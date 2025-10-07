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

class PromptCarveInput(BaseModel):
    kaitiaki: str
    prompt_name: str
    prompt_data: dict

class PromptOptimizeInput(BaseModel):
    kaitiaki: str
    prompt_name: str
    optimization_notes: str

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

@router.get("/prompts")
async def get_prompt_hub_status():
    """Kākā's prompt hub status - central prompt coordinator"""
    return kaka.get_prompt_hub_status()

@router.get("/prompts/{kaitiaki}")
async def get_kaitiaki_prompts(kaitiaki: str):
    """Get all prompts for a specific kaitiaki"""
    prompts = kaka.get_all_prompts_for_kaitiaki(kaitiaki)
    return {
        "kaitiaki": kaka.name,
        "target_kaitiaki": kaitiaki,
        "prompts": prompts
    }

@router.get("/prompts/{kaitiaki}/{prompt_name}")
async def get_specific_prompt(kaitiaki: str, prompt_name: str):
    """Get a specific prompt for a kaitiaki"""
    prompt = kaka.get_prompt(kaitiaki, prompt_name)
    return {
        "kaitiaki": kaka.name,
        "target_kaitiaki": kaitiaki,
        "prompt_name": prompt_name,
        "prompt": prompt
    }

@router.post("/carve-prompt")
async def carve_prompt(data: PromptCarveInput):
    """Kākā carves a new prompt for a kaitiaki"""
    result = kaka.carve_prompt(data.kaitiaki, data.prompt_name, data.prompt_data)
    return {
        "kaitiaki": kaka.name,
        "action": "prompt_carved",
        "target_kaitiaki": data.kaitiaki,
        "prompt_name": data.prompt_name,
        "result": result
    }

@router.post("/optimize-prompt")
async def optimize_prompt(data: PromptOptimizeInput):
    """Kākā optimizes an existing prompt"""
    result = kaka.optimize_prompt(data.kaitiaki, data.prompt_name, data.optimization_notes)
    return {
        "kaitiaki": kaka.name,
        "action": "prompt_optimized",
        "target_kaitiaki": data.kaitiaki,
        "prompt_name": data.prompt_name,
        "result": result
    }


router = APIRouter(prefix="/kaka")

@router.post("/carve_korito")
async def carve_korito():
    # Logic goes here
    return {"message": "Kākā carved korito.py with fresh env router 🍃"}
