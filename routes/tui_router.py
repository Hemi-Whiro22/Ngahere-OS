from fastapi import APIRouter
from pydantic import BaseModel
from matanga.tui.tui import Tui

router = APIRouter()
tui = Tui()

class VoiceInput(BaseModel):
    text: str
    voice_type: str = "default"

@router.get("/")
async def tui_status():
    """Tūī status - the voice is ready"""
    return {
        "kaitiaki": tui.name,
        "status": "ready",
        "capabilities": ["text_to_speech", "voice_generation", "audio_streaming"]
    }

@router.post("/speak")
async def speak_text(data: VoiceInput):
    """Tūī speaks the text"""
    result = tui.speak(data.text, data.voice_type)
    return {
        "kaitiaki": tui.name,
        "text": data.text,
        "result": result,
        "voice_type": data.voice_type
    }
