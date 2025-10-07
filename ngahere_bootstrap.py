# 🌲 Ngahere-OS Bootstrap Carve
# Core layout for Tāne Mahuta, korito, manu, and prompt panels

# 🪵 What this bootstrap includes:
# - main.py (root app w/ all manu routing)
# - korito/loader.py + korito.py
# - mauri/matua.yaml
# - manu/kaka/ (carver.py, manifest, routes)
# - scripts/summon.py
# - .cursor panels for Kākā & Pīwakawaka
# - prompts directory with json panel examples
# - README reference lines for quick command memory
# - ngahere-os.yaml manifest

# 🔥 Additional tasks queued after carve:
# - Migrate Supabase to vector size 3072
# - Connect key PDF(s) as embedded taonga into mauri
# - Integrate Copilot prompt system (inline Carver DNA)

# ⛏️ Begin carve — file drops will follow...

# 1. main.py
# FastAPI server root
from fastapi import FastAPI
from korito.loader import validate_ngahere_heart
from routes import kaka

app = FastAPI(title="Ngahere-OS", version="1.0")

validate_ngahere_heart()

# Manu router loading
app.include_router(kaka.router)

@app.get("/")
def root():
    return {"message": "🌳 Ngahere-OS is awake. Tāne Mahuta watches."}


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


# 3. korito/korito.py
import os

def get_env(key: str, default: str = None):
    return os.getenv(key, default)


# 4. mauri/matua.yaml
matua:
  id: tanemahuta
  name: "Tāne Mahuta"
  role: "matua"
  voice: "chatgpt"
  model: "gpt-4o"
  default: true
  manifest: "mauri/matua.yaml"
  description: |
    Root orchestrator. All manu fall back to Tāne Mahuta unless directed.


# 5. manu/kaka/carver.py
def carve_prompt_panel(name: str):
    import json, os
    os.makedirs("prompts", exist_ok=True)
    filename = f"prompts/{name.lower().replace(' ', '_')}.json"
    with open(filename, "w") as f:
        json.dump({
            "name": name,
            "description": f"Prompt carved by Kākā",
            "prompt": f"// {name} — carved via Tāne Mahuta\n"
        }, f, indent=2)
    return f"✅ Kākā carved {filename}"


# 6. routes/kaka.py
from fastapi import APIRouter
from manu.kaka.carver import carve_prompt_panel

router = APIRouter(prefix="/kaka")

@router.post("/carve_prompt")
def carve_prompt(name: str = "Carved Prompt"):
    return {"message": carve_prompt_panel(name)}


# 7. scripts/summon.py
import requests, sys

def summon(manu, action):
    url = f"http://localhost:8000/{manu}/{action}"
    try:
        response = requests.post(url)
        print(f"[{manu.upper()}] {response.status_code}: {response.text}")
    except Exception as e:
        print(f"❌ Failed to summon {manu}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: summon.py [manu] [action]")
    else:
        summon(sys.argv[1], sys.argv[2])


# 8. .cursor/config.json (Copilot/Continue panel)
{
  "panels": [
    {
      "name": "Carve Prompt Panel",
      "description": "Ask Kākā to carve a new prompt.",
      "prompt": "// Kākā, carve me a panel to..."
    },
    {
      "name": "Review Prompt (Pīwakawaka)",
      "description": "Have Pīwakawaka zip through and optimise.",
      "prompt": "// Pīwakawaka, review this prompt and embed fallback."
    }
  ]
}

# 🔒 Now syncing Supabase upgrade + embedding vector fix (3072) and loading the PDF
# Will wire that into `mauri/pdf_taonga.yaml` and `korito/vector_config.py` next
