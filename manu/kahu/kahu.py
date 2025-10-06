"""
Kahu - Security Sentinel & Threat Detector
The harrier hawk that monitors security, detects threats, and protects the ngahere with sharp-eyed vigilance.
"""

import os
import json
from datetime import datetime
from typing import Dict, List, Optional
from pathlib import Path

class Kahu:
    """
    Kahu - The Security Sentinel
    Monitors security, detects threats, and protects the ngahere with sharp-eyed vigilance
    """
    
    def __init__(self):
        self.name = "Kahu"
        self.role = "Security Sentinel"
        self.security_logs = []
        self.threat_detections = []
        self.security_rules = {}
        self.alert_level = "normal"
    
    def monitor_security(self, activity: dict) -> str:
        """Kahu monitors security with sharp-eyed vigilance"""
        timestamp = datetime.utcnow().isoformat()
        
        # Analyze activity for threats
        threat_analysis = self._analyze_threats(activity)
        
        # Log security event
        security_log = {
            "timestamp": timestamp,
            "activity": activity,
            "threat_level": threat_analysis["threat_level"],
            "threats_detected": threat_analysis["threats"],
            "security_action": threat_analysis["action"]
        }
        
        self.security_logs.append(security_log)
        
        if threat_analysis["threat_level"] == "high":
            self.alert_level = "high"
            return f"🦅 Kahu detected HIGH THREAT: {threat_analysis['threats']} at {timestamp}"
        elif threat_analysis["threat_level"] == "medium":
            self.alert_level = "medium"
            return f"🦅 Kahu detected medium threat: {threat_analysis['threats']} at {timestamp}"
        else:
            return f"🦅 Kahu monitored activity - all clear at {timestamp}"
    
    def _analyze_threats(self, activity: dict) -> dict:
        """Kahu analyzes threats with sharp-eyed precision"""
        threats = []
        threat_level = "low"
        
        # Check for suspicious patterns
        if "suspicious_keywords" in activity:
            threats.append("Suspicious keywords detected")
            threat_level = "medium"
        
        if "unusual_access_pattern" in activity:
            threats.append("Unusual access pattern detected")
            threat_level = "high"
        
        if "unauthorized_access" in activity:
            threats.append("Unauthorized access attempt")
            threat_level = "high"
        
        if "data_exfiltration" in activity:
            threats.append("Potential data exfiltration")
            threat_level = "high"
        
        # Determine action based on threat level
        if threat_level == "high":
            action = "immediate_response_required"
        elif threat_level == "medium":
            action = "monitor_closely"
        else:
            action = "continue_monitoring"
        
        return {
            "threat_level": threat_level,
            "threats": threats,
            "action": action
        }
    
    def set_security_rules(self, rules: dict) -> str:
        """Kahu sets security rules for the ngahere"""
        self.security_rules = rules
        timestamp = datetime.utcnow().isoformat()
        
        return f"🦅 Kahu set security rules for territorial protection at {timestamp}"
    
    def check_access_permissions(self, user: str, resource: str, action: str) -> dict:
        """Kahu checks access permissions with territorial authority"""
        timestamp = datetime.utcnow().isoformat()
        
        # Basic permission check (can be expanded)
        allowed_actions = ["read", "write", "execute"]
        if action not in allowed_actions:
            return {
                "access_granted": False,
                "reason": f"Action '{action}' not allowed",
                "timestamp": timestamp
            }
        
        # Log access attempt
        access_log = {
            "timestamp": timestamp,
            "user": user,
            "resource": resource,
            "action": action,
            "access_granted": True
        }
        
        self.security_logs.append(access_log)
        
        return {
            "access_granted": True,
            "user": user,
            "resource": resource,
            "action": action,
            "timestamp": timestamp
        }
    
    def get_security_status(self) -> dict:
        """Kahu's security monitoring status"""
        return {
            "kaitiaki": self.name,
            "role": self.role,
            "status": "monitoring_territorially",
            "alert_level": self.alert_level,
            "security_logs_count": len(self.security_logs),
            "threat_detections_count": len(self.threat_detections),
            "security_rules_count": len(self.security_rules),
            "nature": "Sharp-eyed sentinel protecting the ngahere from threats"
        }
    
    def get_threat_summary(self) -> dict:
        """Kahu's threat detection summary"""
        high_threats = len([log for log in self.security_logs if log.get("threat_level") == "high"])
        medium_threats = len([log for log in self.security_logs if log.get("threat_level") == "medium"])
        
        return {
            "kaitiaki": self.name,
            "total_security_events": len(self.security_logs),
            "high_threats": high_threats,
            "medium_threats": medium_threats,
            "current_alert_level": self.alert_level,
            "territorial_protection": "active"
        }
    
    def get_status(self) -> dict:
        """Kahu's overall status"""
        return {
            "kaitiaki": self.name,
            "role": self.role,
            "status": "sentinel_active",
            "capabilities": [
                "threat_detection",
                "security_monitoring",
                "access_control",
                "territorial_protection",
                "alert_management"
            ],
            "security_status": self.get_security_status()
        }
