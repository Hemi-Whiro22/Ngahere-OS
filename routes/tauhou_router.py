from fastapi import APIRouter
from pydantic import BaseModel
from kaitiaki.tauhou.tauhou import Tauhou

router = APIRouter()
tauhou = Tauhou()

class AlertThresholdsInput(BaseModel):
    thresholds: dict

@router.get("/")
async def tauhou_status():
    """Tauhou status - the health monitor is observing"""
    return tauhou.get_status()

@router.get("/health")
async def get_health_summary():
    """Tauhou's health monitoring summary"""
    return tauhou.get_health_summary()

@router.post("/monitor")
async def monitor_health():
    """Tauhou monitors system health"""
    result = tauhou.monitor_health()
    return {
        "kaitiaki": tauhou.name,
        "action": "health_monitored",
        "result": result
    }

@router.post("/thresholds")
async def set_alert_thresholds(data: AlertThresholdsInput):
    """Tauhou sets alert thresholds"""
    result = tauhou.set_alert_thresholds(data.thresholds)
    return {
        "kaitiaki": tauhou.name,
        "action": "thresholds_set",
        "result": result
    }
