"""
Cloud Kaitiaki - Flexible AI Model Provider System
Supports multiple AI providers with automatic fallback and model switching
"""

import os
import requests
import json
from typing import Dict, List, Optional, Union
from enum import Enum
from abc import ABC, abstractmethod
from pathlib import Path
import sys

# Add korito to path
sys.path.append(str(Path(__file__).parent / "korito"))
from loader import korito, get_korito_secret

class AIProvider(Enum):
    """Supported AI providers"""
    OPENAI = "openai"
    OLLAMA = "ollama"
    ANTHROPIC = "anthropic"
    GOOGLE = "google"
    AZURE = "azure"

class ModelConfig:
    """Configuration for a specific model"""
    def __init__(self, name: str, provider: AIProvider, endpoint: str, 
                 api_key: str = None, max_tokens: int = 4000, 
                 temperature: float = 0.7, **kwargs):
        self.name = name
        self.provider = provider
        self.endpoint = endpoint
        self.api_key = api_key
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.kwargs = kwargs

class AIProviderInterface(ABC):
    """Abstract interface for AI providers"""
    
    @abstractmethod
    def generate(self, prompt: str, model_config: ModelConfig) -> str:
        pass
    
    @abstractmethod
    def is_available(self) -> bool:
        pass

class OpenAIProvider(AIProviderInterface):
    """OpenAI API provider"""
    
    def generate(self, prompt: str, model_config: ModelConfig) -> str:
        try:
            response = requests.post(
                f"{model_config.endpoint}/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {model_config.api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": model_config.name,
                    "messages": [{"role": "user", "content": prompt}],
                    "max_tokens": model_config.max_tokens,
                    "temperature": model_config.temperature
                },
                timeout=30
            )
            
            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]
            else:
                raise Exception(f"OpenAI API error: {response.text}")
                
        except Exception as e:
            raise Exception(f"OpenAI generation failed: {str(e)}")
    
    def is_available(self) -> bool:
        return get_korito_secret("OPENAI_API_KEY") is not None

class OllamaProvider(AIProviderInterface):
    """Ollama local provider"""
    
    def generate(self, prompt: str, model_config: ModelConfig) -> str:
        try:
            response = requests.post(
                f"{model_config.endpoint}/api/generate",
                json={
                    "model": model_config.name,
                    "prompt": prompt,
                    "stream": False,
                    "options": {
                        "temperature": model_config.temperature,
                        "num_predict": model_config.max_tokens
                    }
                },
                timeout=120
            )
            
            if response.status_code == 200:
                return response.json().get("response", "No response from Ollama")
            else:
                raise Exception(f"Ollama API error: {response.text}")
                
        except Exception as e:
            raise Exception(f"Ollama generation failed: {str(e)}")
    
    def is_available(self) -> bool:
        try:
            ollama_url = get_korito_secret("OLLAMA_URL") or "http://localhost:11434"
            response = requests.get(f"{ollama_url}/api/tags", timeout=5)
            return response.status_code == 200
        except:
            return False

class CloudKaitiaki:
    """
    Cloud Kaitiaki - Intelligent model provider with automatic fallback
    """
    
    def __init__(self):
        self.name = "Cloud Kaitiaki"
        self.providers = {
            AIProvider.OPENAI: OpenAIProvider(),
            AIProvider.OLLAMA: OllamaProvider()
        }
        self.model_configs = self._load_model_configs()
        self.current_provider = None
        self.fallback_chain = [AIProvider.OPENAI, AIProvider.OLLAMA]
    
    def _load_model_configs(self) -> Dict[str, ModelConfig]:
        """Load model configurations from Korito's heart"""
        configs = {}
        
        # OpenAI models (from Korito)
        openai_key = get_korito_secret("OPENAI_API_KEY")
        if openai_key:
            configs["gpt-4"] = ModelConfig(
                name="gpt-4",
                provider=AIProvider.OPENAI,
                endpoint="https://api.openai.com",
                api_key=openai_key
            )
            configs["gpt-3.5-turbo"] = ModelConfig(
                name="gpt-3.5-turbo",
                provider=AIProvider.OPENAI,
                endpoint="https://api.openai.com",
                api_key=openai_key
            )
        
        # Ollama models (from Korito)
        ollama_url = get_korito_secret("OLLAMA_URL") or "http://localhost:11434"
        configs["llama3"] = ModelConfig(
            name="llama3",
            provider=AIProvider.OLLAMA,
            endpoint=ollama_url
        )
        configs["codellama"] = ModelConfig(
            name="codellama",
            provider=AIProvider.OLLAMA,
            endpoint=ollama_url
        )
        
        return configs
    
    def get_available_models(self) -> List[str]:
        """Get list of available models"""
        available = []
        for name, config in self.model_configs.items():
            provider = self.providers[config.provider]
            if provider.is_available():
                available.append(name)
        return available
    
    def generate_with_fallback(self, prompt: str, preferred_model: str = None) -> str:
        """Generate text with automatic fallback between providers"""
        
        # Try preferred model first
        if preferred_model and preferred_model in self.model_configs:
            config = self.model_configs[preferred_model]
            provider = self.providers[config.provider]
            
            if provider.is_available():
                try:
                    return provider.generate(prompt, config)
                except Exception as e:
                    print(f"Preferred model {preferred_model} failed: {e}")
        
        # Try fallback chain
        for provider_type in self.fallback_chain:
            for name, config in self.model_configs.items():
                if config.provider == provider_type:
                    provider = self.providers[provider_type]
                    if provider.is_available():
                        try:
                            return provider.generate(prompt, config)
                        except Exception as e:
                            print(f"Provider {provider_type} failed: {e}")
                            continue
        
        raise Exception("No available AI providers found")
    
    def switch_provider(self, provider_type: AIProvider) -> bool:
        """Manually switch to a specific provider"""
        if provider_type in self.providers:
            provider = self.providers[provider_type]
            if provider.is_available():
                self.current_provider = provider_type
                return True
        return False
    
    def get_status(self) -> Dict:
        """Get status of all providers and models"""
        status = {
            "cloud_kaitiaki": self.name,
            "available_providers": [],
            "available_models": [],
            "current_provider": self.current_provider.value if self.current_provider else None
        }
        
        for provider_type, provider in self.providers.items():
            if provider.is_available():
                status["available_providers"].append(provider_type.value)
        
        status["available_models"] = self.get_available_models()
        
        return status
