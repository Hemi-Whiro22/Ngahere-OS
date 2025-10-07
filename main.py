# 1. main.py
# FastAPI server root
from fastapi import FastAPI
from korito.loader import validate_ngahere_heart
from routes import kaka

app = FastAPI(title="Ngahere-OS", version="1.0")

validate_ngahere_heart()

# Manu router loading
app.include_router(kaka.router)

@app.get("/")
def root():
    return {"message": "🌳 Ngahere-OS is awake. Tāne Mahuta watches."}
