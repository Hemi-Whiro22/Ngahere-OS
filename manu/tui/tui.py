class Tui:
    def __init__(self):
        self.name = "Tūī"

    def speak(self, text: str, voice_type: str = "default") -> str:
        """Tūī speaks the text"""
        return f"🎶 Tūī speaks: {text} (voice: {voice_type})"