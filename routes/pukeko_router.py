from fastapi import APIRouter
from pydantic import BaseModel
from manu.pukeko.pukeko import Pukeko
from typing import Optional

router = APIRouter()
pukeko = Pukeko()

class DataProtectionInput(BaseModel):
    data: dict
    validation_rules: Optional[dict] = None

class BackupInput(BaseModel):
    data: dict
    backup_name: Optional[str] = None

class RestoreInput(BaseModel):
    backup_name: str

@router.get("/")
async def pukeko_status():
    """Pūkeko status - the data guardian is protecting"""
    return pukeko.get_status()

@router.get("/protection")
async def get_protection_status():
    """Pūkeko's data protection status"""
    return pukeko.get_data_protection_status()

@router.post("/protect")
async def protect_data(data: DataProtectionInput):
    """Pūkeko protects data with territorial vigilance"""
    result = pukeko.protect_data(data.data, data.validation_rules)
    return {
        "kaitiaki": pukeko.name,
        "action": "data_protected",
        "result": result
    }

@router.post("/backup")
async def create_backup(data: BackupInput):
    """Pūkeko creates territorial backup"""
    result = pukeko.create_backup(data.data, data.backup_name)
    return {
        "kaitiaki": pukeko.name,
        "action": "backup_created",
        "result": result
    }

@router.post("/restore")
async def restore_backup(data: RestoreInput):
    """Pūkeko restores data from backup"""
    result = pukeko.restore_backup(data.backup_name)
    return {
        "kaitiaki": pukeko.name,
        "action": "backup_restored",
        "result": result
    }
