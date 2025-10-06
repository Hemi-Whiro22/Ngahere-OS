from fastapi import APIRouter
from pydantic import BaseModel
from matanga.kotare.kotare import Kotare

router = APIRouter()
kotare = Kotare()

class TextInput(BaseModel):
    text: str

@router.get("/")
async def kotare_status():
    """Kotare status - the embedder is ready"""
    return {
        "kaitiaki": kotare.name,
        "status": "ready",
        "capabilities": ["embedding", "vector_search", "memory_storage"]
    }

@router.post("/embed")
async def embed_text(data: TextInput):
    """Kotare embeds text into vectors"""
    result = kotare.embed(data.text)
    return {
        "kaitiaki": kotare.name,
        "text": data.text,
        "result": result
    }
