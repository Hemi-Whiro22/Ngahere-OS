class Ruru:
    def __init__(self):
        self.name = "Ruru"

    def summarise(self, text: str) -> str:
        """Ruru summarises text with wisdom"""
        return f"Ruru summarises: {text[:100]}..."