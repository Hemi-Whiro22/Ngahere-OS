# 2. korito/loader.py
from dotenv import load_dotenv
from pathlib import Path
import os


def validate_ngahere_heart():
root = Path(__file__).resolve().parents[1]
env_path = root / ".env"
mauri_path = root / "mauri" / "matua.yaml"


if not env_path.exists():
raise FileNotFoundError("❌ .env not found. The korito is dry.")


if not mauri_path.exists():
raise FileNotFoundError("❌ Matua missing. The ngahere has no heart.")


load_dotenv(dotenv_path=env_path)
print("✅ Korito flowing. Mauri confirmed.")

def get_korito_secret(key: str) -> str:
    """Retrieve a secret from the .env file"""
    return os.getenv(key, "")