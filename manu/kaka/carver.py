# manu/kaka/carver.py

def carve_prompt_panel(name: str):
    filename = f"prompts/{name.lower().replace(' ', '_')}.json"
    prompt_data = {
        "name": name,
        "description": "A prompt carved by Kākā",
        "prompt": f"// {name} — carved via Tāne Mahuta\n"
    }

    with open(filename, "w") as f:
        import json
        json.dump(prompt_data, f, indent=2)

    return f"✅ Kākā carved prompt panel: {filename}"
