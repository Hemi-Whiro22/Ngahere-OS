# 6. routes/kaka.py
from fastapi import APIRouter
from manu.kaka.carver import carve_prompt_panel

router = APIRouter(prefix="/kaka")

@router.post("/carve_prompt")
def carve_prompt(name: str = "Carved Prompt"):
    return {"message": carve_prompt_panel(name)}