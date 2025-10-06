"""
Riroriro - Communication Coordinator & Message Guardian
The grey warbler that handles notifications, alerts, and communication between kaitiaki with powerful voice.
"""

import os
import json
from datetime import datetime
from typing import Dict, List, Optional
from pathlib import Path

class Riroriro:
    """
    Riroriro - The Communication Coordinator
    Handles notifications, alerts, and communication between kaitiaki with powerful voice
    """
    
    def __init__(self):
        self.name = "Riroriro"
        self.role = "Communication Coordinator"
        self.message_logs = []
        self.notification_queue = []
        self.communication_channels = {}
    
    def send_notification(self, message: str, recipient: str = "all", priority: str = "normal") -> str:
        """Riroriro sends notifications with powerful voice"""
        timestamp = datetime.utcnow().isoformat()
        
        notification = {
            "timestamp": timestamp,
            "message": message,
            "recipient": recipient,
            "priority": priority,
            "status": "sent"
        }
        
        self.message_logs.append(notification)
        self.notification_queue.append(notification)
        
        return f"🐦 Riroriro sent notification to {recipient}: {message} at {timestamp}"
    
    def broadcast_alert(self, alert_type: str, message: str, urgency: str = "normal") -> str:
        """Riroriro broadcasts alerts to all kaitiaki"""
        timestamp = datetime.utcnow().isoformat()
        
        alert = {
            "timestamp": timestamp,
            "alert_type": alert_type,
            "message": message,
            "urgency": urgency,
            "broadcast": True
        }
        
        self.message_logs.append(alert)
        
        urgency_emoji = "🔴" if urgency == "high" else "🟡" if urgency == "medium" else "🟢"
        
        return f"🐦 Riroriro broadcast {urgency_emoji} {alert_type} alert: {message} at {timestamp}"
    
    def coordinate_kaitiaki_communication(self, sender: str, receiver: str, message: str) -> str:
        """Riroriro coordinates communication between kaitiaki"""
        timestamp = datetime.utcnow().isoformat()
        
        communication = {
            "timestamp": timestamp,
            "sender": sender,
            "receiver": receiver,
            "message": message,
            "coordinated_by": self.name
        }
        
        self.message_logs.append(communication)
        
        return f"🐦 Riroriro coordinated communication: {sender} → {receiver}: {message} at {timestamp}"
    
    def get_communication_status(self) -> dict:
        """Riroriro's communication status"""
        return {
            "kaitiaki": self.name,
            "role": self.role,
            "status": "coordinating_communication",
            "total_messages": len(self.message_logs),
            "pending_notifications": len(self.notification_queue),
            "active_channels": len(self.communication_channels),
            "nature": "Powerful voice coordinating communication across the ngahere"
        }
    
    def get_message_summary(self) -> dict:
        """Riroriro's message coordination summary"""
        if not self.message_logs:
            return {
                "kaitiaki": self.name,
                "status": "no_messages",
                "message": "No communication data available yet"
            }
        
        # Count message types
        notifications = len([msg for msg in self.message_logs if "recipient" in msg])
        alerts = len([msg for msg in self.message_logs if "alert_type" in msg])
        communications = len([msg for msg in self.message_logs if "sender" in msg])
        
        return {
            "kaitiaki": self.name,
            "total_messages": len(self.message_logs),
            "notifications": notifications,
            "alerts": alerts,
            "kaitiaki_communications": communications,
            "pending_queue": len(self.notification_queue)
        }
    
    def get_status(self) -> dict:
        """Riroriro's overall status"""
        return {
            "kaitiaki": self.name,
            "role": self.role,
            "status": "coordinating_actively",
            "capabilities": [
                "notification_management",
                "alert_broadcasting",
                "kaitiaki_coordination",
                "message_routing",
                "communication_guardian"
            ],
            "communication_status": self.get_communication_status()
        }
