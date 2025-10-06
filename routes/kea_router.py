from fastapi import APIRouter
from pydantic import BaseModel
from kaitiaki.kea.kea import Kea

router = APIRouter()
kea = Kea()

class PromptInput(BaseModel):
    prompt: str

class CodeInput(BaseModel):
    code: str

@router.post("/optimize")
async def optimize_prompt(data: PromptInput):
    return {"kaitiaki": kea.name, "result": kea.optimize(data.prompt)}

@router.post("/stress")
async def stress_test(data: CodeInput):
    return {"kaitiaki": kea.name, "result": kea.stress_test(data.code)}
