"""
Pūkeko - Data Guardian & Protector
The swamp hen that guards data integrity, backup systems, and data validation with territorial protection.
"""

import os
import json
from datetime import datetime
from typing import Dict, List, Optional
from pathlib import Path

class Pukeko:
    """
    Pūkeko - The Data Guardian
    Protects data integrity, manages backups, and validates data with territorial protection
    """
    
    def __init__(self):
        self.name = "Pūkeko"
        self.role = "Data Guardian"
        self.data_logs = []
        self.backup_status = {}
        self.validation_rules = {}
    
    def protect_data(self, data: dict, validation_rules: Optional[dict] = None) -> str:
        """Pūkeko protects data with territorial vigilance"""
        validation_rules = validation_rules or {}
        timestamp = datetime.utcnow().isoformat()
        
        # Validate data integrity
        validation_result = self._validate_data_integrity(data, validation_rules)
        
        # Log protection action
        protection_log = {
            "timestamp": timestamp,
            "action": "data_protected",
            "data_size": len(str(data)),
            "validation_passed": validation_result["valid"],
            "protection_level": "territorial_guardian"
        }
        
        self.data_logs.append(protection_log)
        
        if validation_result["valid"]:
            return f"🦆 Pūkeko protected data with territorial vigilance at {timestamp}"
        else:
            return f"🦆 Pūkeko detected data issues: {validation_result['issues']}"
    
    def _validate_data_integrity(self, data: dict, rules: dict = None) -> dict:
        """Pūkeko validates data integrity with territorial precision"""
        issues = []
        
        # Basic validation
        if not isinstance(data, dict):
            issues.append("Data must be a dictionary")
        
        # Check for required fields
        if rules and "required_fields" in rules:
            for field in rules["required_fields"]:
                if field not in data:
                    issues.append(f"Missing required field: {field}")
        
        # Check data types
        if rules and "type_checks" in rules:
            for field, expected_type in rules["type_checks"].items():
                if field in data and not isinstance(data[field], expected_type):
                    issues.append(f"Field {field} should be {expected_type.__name__}")
        
        return {
            "valid": len(issues) == 0,
            "issues": issues
        }
    
    def create_backup(self, data: dict, backup_name: Optional[str] = None) -> str:
        """Pūkeko creates territorial backup of data"""
        backup_name = backup_name or f"backup_{datetime.utcnow().isoformat().replace(':', '-')}"

        timestamp = datetime.utcnow().isoformat()
        
        try:
            # Create backup directory
            backup_dir = Path(__file__).parent / "backups"
            backup_dir.mkdir(exist_ok=True)
            
            # Save backup
            backup_file = backup_dir / f"{backup_name}.json"
            with open(backup_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            
            # Update backup status
            self.backup_status[backup_name] = {
                "timestamp": timestamp,
                "file_path": str(backup_file),
                "data_size": len(str(data)),
                "status": "protected"
            }
            
            return f"🦆 Pūkeko created territorial backup '{backup_name}' at {timestamp}"
            
        except Exception as e:
            return f"Pūkeko couldn't create backup: {str(e)}"
    
    def restore_backup(self, backup_name: str) -> dict:
        """Pūkeko restores data from territorial backup"""
        if backup_name not in self.backup_status:
            return {"error": f"Backup '{backup_name}' not found"}
        
        try:
            backup_file = Path(self.backup_status[backup_name]["file_path"])
            with open(backup_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            return {
                "success": True,
                "data": data,
                "restored_from": backup_name,
                "timestamp": self.backup_status[backup_name]["timestamp"]
            }
            
        except Exception as e:
            return {"error": f"Pūkeko couldn't restore backup: {str(e)}"}
    
    def get_data_protection_status(self) -> dict:
        """Pūkeko's data protection status"""
        return {
            "kaitiaki": self.name,
            "role": self.role,
            "status": "protecting_territorially",
            "data_logs_count": len(self.data_logs),
            "backups_count": len(self.backup_status),
            "protection_level": "territorial_guardian",
            "nature": "Territorial protector of data integrity and backup systems"
        }
    
    def get_status(self) -> dict:
        """Pūkeko's overall status"""
        return {
            "kaitiaki": self.name,
            "role": self.role,
            "status": "guarding_data",
            "capabilities": [
                "data_protection",
                "backup_management", 
                "data_validation",
                "territorial_guardian",
                "integrity_monitoring"
            ],
            "data_protection_status": self.get_data_protection_status()
        }
