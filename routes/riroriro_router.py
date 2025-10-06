from fastapi import APIRouter
from pydantic import BaseModel
from kaitiaki.riroriro.riroriro import Riroriro

router = APIRouter()
riroriro = Riroriro()

class NotificationInput(BaseModel):
    message: str
    recipient: str = "all"
    priority: str = "normal"

class AlertInput(BaseModel):
    alert_type: str
    message: str
    urgency: str = "normal"

class CommunicationInput(BaseModel):
    sender: str
    receiver: str
    message: str

@router.get("/")
async def riroriro_status():
    """Riroriro status - the communication coordinator is active"""
    return riroriro.get_status()

@router.get("/communication")
async def get_communication_status():
    """Riroriro's communication status"""
    return riroriro.get_communication_status()

@router.get("/messages")
async def get_message_summary():
    """Riroriro's message coordination summary"""
    return riroriro.get_message_summary()

@router.post("/notify")
async def send_notification(data: NotificationInput):
    """Riroriro sends notification"""
    result = riroriro.send_notification(data.message, data.recipient, data.priority)
    return {
        "kaitiaki": riroriro.name,
        "action": "notification_sent",
        "result": result
    }

@router.post("/alert")
async def broadcast_alert(data: AlertInput):
    """Riroriro broadcasts alert"""
    result = riroriro.broadcast_alert(data.alert_type, data.message, data.urgency)
    return {
        "kaitiaki": riroriro.name,
        "action": "alert_broadcast",
        "result": result
    }

@router.post("/coordinate")
async def coordinate_communication(data: CommunicationInput):
    """Riroriro coordinates communication between kaitiaki"""
    result = riroriro.coordinate_kaitiaki_communication(data.sender, data.receiver, data.message)
    return {
        "kaitiaki": riroriro.name,
        "action": "communication_coordinated",
        "result": result
    }
