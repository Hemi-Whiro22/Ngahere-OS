from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Optional
import sys
from pathlib import Path

# Add korito to path
sys.path.append(str(Path(__file__).parent.parent / "kaitiaki" / "korito"))
from loader import korito, validate_ngahere_heart, get_korito_secret

router = APIRouter()

class SecretRequest(BaseModel):
    key: str

class SecretResponse(BaseModel):
    kaitiaki: str
    secret_key: str
    value: Optional[str]
    status: str

@router.get("/")
async def korito_status():
    """Korito status - the heart of the forest"""
    return korito.get_status()

@router.get("/heartbeat")
async def heartbeat():
    """Check if Korito's heart is beating (essential for ngahere)"""
    is_healthy = validate_ngahere_heart()
    return {
        "kaitiaki": korito.name,
        "heartbeat": "strong" if is_healthy else "weak",
        "ngahere_can_function": is_healthy,
        "message": "Korito's heart beats strong" if is_healthy else "Korito's heart is weak"
    }

@router.get("/secrets")
async def get_secrets_overview():
    """Get overview of all secrets (without revealing values)"""
    status = korito.get_status()
    return {
        "kaitiaki": korito.name,
        "secrets_loaded": status.get("secrets_loaded", False),
        "secrets_count": status.get("secrets_count", 0),
        "available_secrets": status.get("available_secrets", []),
        "env_path": status.get("env_path", "unknown")
    }

@router.post("/secret")
async def get_secret(data: SecretRequest):
    """Get a specific secret from Korito's heart (use carefully!)"""
    try:
        secret_value = get_korito_secret(data.key)
        return SecretResponse(
            kaitiaki=korito.name,
            secret_key=data.key,
            value=secret_value,
            status="found" if secret_value else "not_found"
        )
    except Exception as e:
        return SecretResponse(
            kaitiaki=korito.name,
            secret_key=data.key,
            value=None,
            status=f"error: {str(e)}"
        )

@router.get("/validate")
async def validate_heart():
    """Validate Korito's heart and essential secrets"""
    is_valid = validate_ngahere_heart()
    return {
        "kaitiaki": korito.name,
        "heart_valid": is_valid,
        "ngahere_status": "healthy" if is_valid else "unhealthy",
        "message": "Korito's heart is strong and the ngahere can function" if is_valid else "Korito's heart needs attention"
    }
