from fastapi import APIRouter
from pydantic import BaseModel
from matanga.kaka.kaka import Kaka

router = APIRouter()
kaka = Kaka()

class CarveInput(BaseModel):
    target: str
    context: str = ""

@router.get("/")
async def kaka_status():
    """Kākā status - the carver is ready"""
    return {
        "kaitiaki": kaka.name,
        "status": "ready",
        "capabilities": ["carve", "code_generation", "inline_completion"]
    }

@router.post("/carve")
async def carve_code(data: CarveInput):
    """Kākā carves code based on target and context"""
    result = kaka.carve(data.target)
    return {
        "kaitiaki": kaka.name,
        "target": data.target,
        "result": result,
        "context": data.context
    }