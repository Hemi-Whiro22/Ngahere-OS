from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def call():
    return {"katiaki": "Tūī", "role": "Voice of the ngahere - reo & speech"}
