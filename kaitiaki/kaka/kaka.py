import sys
import os
from pathlib import Path

# Add parent directory to path to import cloud_kaitiaki and korito
sys.path.append(str(Path(__file__).parent.parent))
from cloud_kaitiaki import CloudKaitiaki, AIProvider
from korito.loader import get_korito_secret
from kaka.prompt_hub import prompt_hub

class Kaka:
    def __init__(self):
        self.name = "Kaka"
        self.role = "Carver & Prompt Coordinator"
        self.cloud_kaitiaki = CloudKaitiaki()
        # Get preferred model from Korito's heart
        self.preferred_model = get_korito_secret("KAKA_PREFERRED_MODEL") or "gpt-4"
        # Kākā manages the central prompt hub
        self.prompt_hub = prompt_hub

    def carve(self, target: str, context: str = "", model: str = None) -> str:
        """Kākā carves code using Cloud Kaitiaki with automatic fallback"""
        try:
            # Create a prompt for code generation
            prompt = f"""You are Kaka, the code carver from the ngahere. Generate clean, working code for: {target}

Context: {context}

Requirements:
- Write clean, readable code
- Include comments where helpful
- Make it production-ready
- Use best practices
- Be helpful and clear
- Follow the spirit of kaitiakitanga (guardianship) in your code

Code:"""

            # Use specified model or preferred model
            model_to_use = model or self.preferred_model
            
            # Generate using Cloud Kaitiaki with fallback
            result = self.cloud_kaitiaki.generate_with_fallback(prompt, model_to_use)
            
            return f"🪶 Kākā carved with {model_to_use}:\n\n{result}"
                
        except Exception as e:
            return f"Kākā couldn't carve (Cloud Kaitiaki error): {str(e)}"
    
    def get_available_models(self) -> list:
        """Get list of available models for carving"""
        return self.cloud_kaitiaki.get_available_models()
    
    def switch_model(self, model: str) -> bool:
        """Switch to a specific model"""
        available_models = self.get_available_models()
        if model in available_models:
            self.preferred_model = model
            return True
        return False
    
    def carve_prompt(self, kaitiaki: str, prompt_name: str, prompt_data: dict) -> str:
        """Kākā carves a new prompt for a kaitiaki"""
        success = self.prompt_hub.carve_new_prompt(kaitiaki, prompt_name, prompt_data)
        if success:
            return f"🪶 Kākā carved prompt '{prompt_name}' for {kaitiaki}"
        else:
            return f"Kākā couldn't carve prompt '{prompt_name}' for {kaitiaki}"
    
    def get_prompt(self, kaitiaki: str, prompt_name: str) -> dict:
        """Kākā retrieves a prompt for a kaitiaki"""
        return self.prompt_hub.get_prompt(kaitiaki, prompt_name)
    
    def get_all_prompts_for_kaitiaki(self, kaitiaki: str) -> dict:
        """Kākā gets all prompts for a kaitiaki"""
        return self.prompt_hub.get_all_prompts_for_kaitiaki(kaitiaki)
    
    def optimize_prompt(self, kaitiaki: str, prompt_name: str, optimization_notes: str) -> str:
        """Kākā optimizes an existing prompt"""
        success = self.prompt_hub.optimize_prompt(kaitiaki, prompt_name, optimization_notes)
        if success:
            return f"🪶 Kākā optimized prompt '{prompt_name}' for {kaitiaki}"
        else:
            return f"Kākā couldn't optimize prompt '{prompt_name}' for {kaitiaki}"
    
    def get_prompt_hub_status(self) -> dict:
        """Kākā's prompt hub status"""
        return self.prompt_hub.get_status()
    
    def get_status(self) -> dict:
        """Get Kākā's status and available models"""
        return {
            "kaitiaki": self.name,
            "role": self.role,
            "status": "ready",
            "capabilities": [
                "carve", "code_generation", "model_switching", "cloud_fallback",
                "prompt_carving", "prompt_coordination", "prompt_optimization"
            ],
            "preferred_model": self.preferred_model,
            "available_models": self.get_available_models(),
            "cloud_kaitiaki_status": self.cloud_kaitiaki.get_status(),
            "prompt_hub_status": self.prompt_hub.get_status()
        }
