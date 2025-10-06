from fastapi import APIRouter
from pydantic import BaseModel
from kaitiaki.kaka.kaka import Kaka

router = APIRouter()
kaka = Kaka()

class CarveInput(BaseModel):
    target: str
    context: str = ""
    model: str = None

class ModelSwitchInput(BaseModel):
    model: str

@router.get("/")
async def kaka_status():
    """Kākā status - the carver is ready with Cloud Kaitiaki"""
    return kaka.get_status()

@router.get("/models")
async def get_available_models():
    """Get available AI models for carving"""
    return {
        "kaitiaki": kaka.name,
        "available_models": kaka.get_available_models(),
        "preferred_model": kaka.preferred_model
    }

@router.post("/carve")
async def carve_code(data: CarveInput):
    """Kākā carves code with Cloud Kaitiaki and automatic fallback"""
    result = kaka.carve(data.target, data.context, data.model)
    return {
        "kaitiaki": kaka.name,
        "target": data.target,
        "result": result,
        "context": data.context,
        "model_used": data.model or kaka.preferred_model
    }

@router.post("/switch-model")
async def switch_model(data: ModelSwitchInput):
    """Switch Kākā to a different AI model"""
    success = kaka.switch_model(data.model)
    return {
        "kaitiaki": kaka.name,
        "model_switched": data.model,
        "success": success,
        "current_model": kaka.preferred_model if success else "unchanged"
    }