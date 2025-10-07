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