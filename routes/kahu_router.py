from fastapi import APIRouter
from pydantic import BaseModel
from kaitiaki.kahu.kahu import Kahu

router = APIRouter()
kahu = Kahu()

class SecurityMonitoringInput(BaseModel):
    activity: dict

class SecurityRulesInput(BaseModel):
    rules: dict

class AccessCheckInput(BaseModel):
    user: str
    resource: str
    action: str

@router.get("/")
async def kahu_status():
    """Kahu status - the security sentinel is watching"""
    return kahu.get_status()

@router.get("/security")
async def get_security_status():
    """Kahu's security monitoring status"""
    return kahu.get_security_status()

@router.get("/threats")
async def get_threat_summary():
    """Kahu's threat detection summary"""
    return kahu.get_threat_summary()

@router.post("/monitor")
async def monitor_security(data: SecurityMonitoringInput):
    """Kahu monitors security with sharp-eyed vigilance"""
    result = kahu.monitor_security(data.activity)
    return {
        "kaitiaki": kahu.name,
        "action": "security_monitored",
        "result": result
    }

@router.post("/rules")
async def set_security_rules(data: SecurityRulesInput):
    """Kahu sets security rules"""
    result = kahu.set_security_rules(data.rules)
    return {
        "kaitiaki": kahu.name,
        "action": "rules_set",
        "result": result
    }

@router.post("/access")
async def check_access(data: AccessCheckInput):
    """Kahu checks access permissions"""
    result = kahu.check_access_permissions(data.user, data.resource, data.action)
    return {
        "kaitiaki": kahu.name,
        "action": "access_checked",
        "result": result
    }
