from fastapi import APIRouter
from pydantic import BaseModel
from manu.ruru.ruru import Ruru

router = APIRouter()
ruru = Ruru()

class TextInput(BaseModel):
    text: str

@router.post("/summarise")
async def summarise(data: TextInput):
    return {"kaitiaki": ruru.name, "result": ruru.summarise(data.text)}
