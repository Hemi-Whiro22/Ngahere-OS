from fastapi import APIRouter
from pydantic import BaseModel
from manu.piwakawaka.piwakawaka import Piwakawaka

router = APIRouter()
piwakawaka = Piwakawaka()

class PromptDanceInput(BaseModel):
    kaitiaki: str
    prompt_name: str
    prompt_data: dict

class PromptOptimizeInput(BaseModel):
    kaitiaki: str
    prompt_name: str
    optimization_notes: str

@router.get("/")
async def piwakawaka_status():
    """Pīwakawaka status - zipping around chirping about prompts"""
    return piwakawaka.get_status()

@router.get("/chirp")
async def chirp_about_prompts():
    """Pīwakawaka chirps excessively about all prompts"""
    return piwakawaka.chirp_about_prompts()

@router.get("/prompts/{kaitiaki}")
async def get_kaitiaki_prompts(kaitiaki: str):
    """Pīwakawaka zips around and gets all prompts for a kaitiaki"""
    prompts = piwakawaka.get_all_prompts_for_kaitiaki(kaitiaki)
    return {
        "kaitiaki": piwakawaka.name,
        "target_kaitiaki": kaitiaki,
        "prompts": prompts,
        "chirping": f"Pīwakawaka zipped around and found {len(prompts)} prompts for {kaitiaki}!"
    }

@router.get("/prompts/{kaitiaki}/{prompt_name}")
async def get_specific_prompt(kaitiaki: str, prompt_name: str):
    """Pīwakawaka zips to get a specific prompt"""
    prompt = piwakawaka.get_prompt(kaitiaki, prompt_name)
    return {
        "kaitiaki": piwakawaka.name,
        "target_kaitiaki": kaitiaki,
        "prompt_name": prompt_name,
        "prompt": prompt,
        "chirping": f"Pīwakawaka zipped to {kaitiaki} and found prompt '{prompt_name}'!"
    }

@router.post("/dance")
async def dance_with_prompt(data: PromptDanceInput):
    """Pīwakawaka dances with a prompt (creates or updates)"""
    result = piwakawaka.dance_with_prompt(data.kaitiaki, data.prompt_name, data.prompt_data)
    return {
        "kaitiaki": piwakawaka.name,
        "action": "prompt_dance",
        "target_kaitiaki": data.kaitiaki,
        "prompt_name": data.prompt_name,
        "result": result
    }

@router.post("/zip-optimize")
async def zip_around_optimize(data: PromptOptimizeInput):
    """Pīwakawaka zips around and optimizes a prompt"""
    result = piwakawaka.zip_around_optimize(data.kaitiaki, data.prompt_name, data.optimization_notes)
    return {
        "kaitiaki": piwakawaka.name,
        "action": "zip_optimize",
        "target_kaitiaki": data.kaitiaki,
        "prompt_name": data.prompt_name,
        "result": result
    }
