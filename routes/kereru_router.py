from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
import json

router = APIRouter()

class Kereru:
    """Kererū - Gentle Auditor of the Forest"""
    
    def __init__(self):
        self.name = "Kererū"
        self.role = "Gentle Auditor"
        self.audit_logs = []
    
    def log_action(self, audit_data: dict) -> str:
        """Kererū gently watches and records actions in the forest"""
        timestamp = datetime.utcnow().isoformat()
        audit_entry = {
            "timestamp": timestamp,
            "kaitiaki": audit_data.get("kaitiaki", "unknown"),
            "action": audit_data.get("action", "unknown"),
            "query": audit_data.get("query", ""),
            "result": audit_data.get("result", ""),
            "mana": "gentle_watchfulness"
        }
        
        self.audit_logs.append(audit_entry)
        
        return f"🕊️ Kererū gently recorded: {audit_data.get('action', 'action')} at {timestamp}"
    
    def get_audit_logs(self) -> list:
        """Get all audit logs from Kererū's gentle watch"""
        return self.audit_logs
    
    def get_status(self) -> dict:
        """Get Kererū's gentle status"""
        return {
            "kaitiaki": self.name,
            "role": self.role,
            "status": "watching_gently",
            "capabilities": ["gentle_audit_logging", "provenance_tracking", "mana_recording", "knowledge_spreading"],
            "audit_count": len(self.audit_logs),
            "nature": "Gentle guardian watching over all manu with caring eyes"
        }

# Initialize Kererū
kereru = Kereru()

class AuditLog(BaseModel):
    action: str
    kaitiaki: str
    query: str
    result: str
    timestamp: str = None

@router.get("/")
async def kereru_status():
    """Kererū status - the gentle auditor is watching"""
    return kereru.get_status()

@router.get("/logs")
async def get_audit_logs():
    """Get all audit logs from Kererū's gentle watch"""
    return {
        "kaitiaki": kereru.name,
        "audit_logs": kereru.get_audit_logs(),
        "total_logs": len(kereru.get_audit_logs())
    }

@router.post("/audit")
async def log_action(audit: AuditLog):
    """Kererū gently logs an action in the forest"""
    result = kereru.log_action(audit.dict())
    return {
        "kaitiaki": kereru.name,
        "action_logged": audit.action,
        "result": result,
        "nature": "gentle_watchfulness"
    }
