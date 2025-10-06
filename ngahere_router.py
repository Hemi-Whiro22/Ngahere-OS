import datetime

class Ngahere:
    def __init__(self):
        self.name = "Ngahere"

    def log_action(self, audit_data: dict) -> str:
        """Ngahere logs an action in the forest"""
        timestamp = datetime.datetime.utcnow().isoformat()
        return f"🌲 Ngahere logged: {audit_data['action']} at {timestamp}"