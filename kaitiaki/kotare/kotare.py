class Kotare:
    def __init__(self):
        self.name = "Kotare"

    def embed(self, text: str) -> str:
        """Kotare embeds text into vectors"""
        return f"Kotare embedded: {text[:50]}..."