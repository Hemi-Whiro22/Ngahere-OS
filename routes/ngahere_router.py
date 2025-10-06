from fastapi import APIRouter
from pydantic import BaseModel
from ngahere_router import Ngahere

router = APIRouter()
ngahere = Ngahere()

class AuditLog(BaseModel):
    action: str
    kaitiaki: str
    query: str
    result: str
    timestamp: str = None

@router.get("/")
async def ngahere_status():
    """Ngahere status - the forest auditor is ready"""
    return {
        "kaitiaki": ngahere.name,
        "status": "ready",
        "capabilities": ["audit_logging", "provenance_tracking", "mana_recording"]
    }

@router.post("/audit")
async def log_action(audit: AuditLog):
    """Ngahere logs an action in the forest"""
    result = ngahere.log_action(audit.dict())
    return {
        "kaitiaki": ngahere.name,
        "action_logged": audit.action,
        "result": result
    }
