from fastapi import APIRouter
from pydantic import BaseModel
from kaitiaki.karearea.karearea import Karearea

router = APIRouter()
karearea = Karearea()

class ImageInput(BaseModel):
    image_path: str

@router.get("/")
async def karearea_status():
    """Karearea status - the scanner is ready"""
    return {
        "kaitiaki": karearea.name,
        "status": "ready",
        "capabilities": ["ocr", "image_scanning", "text_extraction"]
    }

@router.post("/scan")
async def scan_image(data: ImageInput):
    """Karearea scans an image with sharp eyesight"""
    result = karearea.scan(data.image_path)
    return {
        "kaitiaki": karearea.name,
        "image_path": data.image_path,
        "result": result
    }