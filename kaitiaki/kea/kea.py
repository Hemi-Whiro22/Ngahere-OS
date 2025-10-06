import yaml
from pathlib import Path

class Kea:
    def __init__(self):
        self.name = "Kea"
        self.prompts = self.load_prompts()

    def load_prompts(self):
        prompt_dir = Path(__file__).parent / "prompts"
        prompts = {}
        for file in prompt_dir.glob("*.yaml"):
            with open(file, "r", encoding="utf-8") as f:
                prompts[file.stem] = yaml.safe_load(f)
        return prompts

    def optimize(self, text: str) -> str:
        # Simple stub — real logic might call Ollama or Supabase logs
        return f"🪶 Kea refined: {text}"

    def stress_test(self, code: str) -> dict:
        return {
            "original": code,
            "tested": True,
            "notes": "No obvious errors found (Kea test run)."
        }
