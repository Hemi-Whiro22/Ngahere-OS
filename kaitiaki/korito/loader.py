import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from typing import Dict, Optional

class Korito:
    """
    Korito - The Heart of the Forest
    Essential kaitiaki that holds all environment secrets.
    Without Korito, the ngahere cannot function.
    """
    
    def __init__(self):
        self.name = "Korito"
        self.role = "Heart of the Forest"
        self.env_path = Path(__file__).parent / ".env"
        self.secrets = {}
        self.is_loaded = False
        
    def load_secrets(self) -> Dict[str, str]:
        """
        Load all secrets from Korito's .env file.
        This is the ONLY place environment variables are loaded from.
        """
        if not self.env_path.exists():
            raise FileNotFoundError(
                f"🌲 KORITO MISSING: The heart of the forest is not found!\n"
                f"Missing .env file at: {self.env_path}\n"
                f"Without Korito, the ngahere cannot function.\n"
                f"Please create the .env file in kaitiaki/korito/ directory."
            )
        
        # Load environment variables from Korito's .env
        load_dotenv(dotenv_path=self.env_path)
        
        # Extract all secrets
        self.secrets = {
            "SUPABASE_URL": os.getenv("SUPABASE_URL"),
            "SUPABASE_KEY": os.getenv("SUPABASE_KEY"),
            "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
            "OLLAMA_URL": os.getenv("OLLAMA_URL", "http://localhost:11434"),
            "OLLAMA_MODEL": os.getenv("OLLAMA_MODEL", "llama3"),
            "KAKA_PREFERRED_MODEL": os.getenv("KAKA_PREFERRED_MODEL", "gpt-4"),
            "RURU_PREFERRED_MODEL": os.getenv("RURU_PREFERRED_MODEL", "gpt-4"),
            "TUI_PREFERRED_MODEL": os.getenv("TUI_PREFERRED_MODEL", "gpt-4"),
            "ANTHROPIC_API_KEY": os.getenv("ANTHROPIC_API_KEY"),
            "GOOGLE_AI_API_KEY": os.getenv("GOOGLE_AI_API_KEY"),
            "APP_NAME": os.getenv("APP_NAME", "Ngahere-OS"),
            "APP_VERSION": os.getenv("APP_VERSION", "0.1.0"),
            "DEBUG": os.getenv("DEBUG", "True").lower() == "true",
            "LOG_LEVEL": os.getenv("LOG_LEVEL", "INFO"),
            "CULTURAL_MODE": os.getenv("CULTURAL_MODE", "True").lower() == "true",
            "LANGUAGE": os.getenv("LANGUAGE", "en_NZ")
        }
        
        self.is_loaded = True
        return self.secrets
    
    def get_secret(self, key: str) -> Optional[str]:
        """Get a specific secret from Korito's heart"""
        if not self.is_loaded:
            self.load_secrets()
        return self.secrets.get(key)
    
    def get_status(self) -> Dict:
        """Get Korito's status and loaded secrets (without revealing values)"""
        if not self.is_loaded:
            try:
                self.load_secrets()
            except FileNotFoundError as e:
                return {
                    "kaitiaki": self.name,
                    "status": "MISSING",
                    "error": str(e),
                    "secrets_loaded": False,
                    "env_path": str(self.env_path)
                }
        
        return {
            "kaitiaki": self.name,
            "role": self.role,
            "status": "active",
            "secrets_loaded": True,
            "secrets_count": len(self.secrets),
            "env_path": str(self.env_path),
            "available_secrets": list(self.secrets.keys())
        }
    
    def validate_essential_secrets(self) -> bool:
        """Validate that essential secrets are present"""
        if not self.is_loaded:
            self.load_secrets()
        
        essential_keys = ["OPENAI_API_KEY"]
        missing_keys = [key for key in essential_keys if not self.secrets.get(key)]
        
        if missing_keys:
            print(f"🌲 KORITO WARNING: Missing essential secrets: {missing_keys}")
            return False
        
        return True

# Global Korito instance - the heart of the forest
korito = Korito()

def load_rito():
    """Legacy function - now uses Korito"""
    return korito.load_secrets()

def get_korito_secret(key: str) -> Optional[str]:
    """Get a secret from Korito's heart"""
    return korito.get_secret(key)

def validate_ngahere_heart() -> bool:
    """Validate that Korito (the heart) is present and functioning"""
    try:
        korito.load_secrets()
        return korito.validate_essential_secrets()
    except Exception as e:
        print(f"🌲 NGAHERE FAILURE: {e}")
        return False
