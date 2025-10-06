from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import sys
from pathlib import Path

# Check for Korito (the heart) before starting
sys.path.append(str(Path(__file__).parent / "kaitiaki" / "korito"))
from loader import validate_ngahere_heart, korito

# Validate that Korito is present and functioning
if not validate_ngahere_heart():
    print("🌲 NGAHERE FAILURE: Korito (the heart) is missing or invalid!")
    print("Please ensure kaitiaki/korito/.env exists with proper configuration.")
    sys.exit(1)

print("🌲 Korito (the heart) is present - the ngahere can function!")

# Import kaitiaki routers
from routes.kea_router import router as kea_router
from routes.ruru_router import router as ruru_router  
from routes.kaka_router import router as kaka_router
from routes.kotare_router import router as kotare_router
from routes.karearea_router import router as karearea_router
from routes.tui_router import router as tui_router
from routes.ngahere_router import router as ngahere_router

app = FastAPI(title="Ngahere-OS - Living Forest of Kaitiaki", version="0.1.0")

# Mount all kaitiaki routers
app.include_router(kea_router, prefix="/kea", tags=["Kea - Search"])
app.include_router(ruru_router, prefix="/ruru", tags=["Ruru - Summaries"])
app.include_router(kaka_router, prefix="/kaka", tags=["Kaka - Carver"])
app.include_router(kotare_router, prefix="/kotare", tags=["Kotare - Embeds"])
app.include_router(karearea_router, prefix="/karearea", tags=["Karearea - OCR"])
app.include_router(tui_router, prefix="/tui", tags=["Tui - Voice"])
app.include_router(ngahere_router, prefix="/ngahere", tags=["Ngahere - Audit"])

@app.get("/")
async def root():
    """Ngahere-OS - The living forest of kaitiaki guardians"""
    return {
        "name": "Ngahere-OS",
        "description": "Living forest of kaitiaki guardians sustained by Tane Mahuta",
        "version": "0.1.0",
        "kaitiaki": ["kea", "ruru", "kaka", "kotare", "karearea", "tui", "ngahere"],
        "endpoints": {
            "kea": "/kea - Searcher (finds things in archives)",
            "ruru": "/ruru - Summariser (brings clarity)", 
            "kaka": "/kaka - Carver (shapes code)",
            "kotare": "/kotare - Embedder (stores knowledge)",
            "karearea": "/karearea - Scanner (sees everything)",
            "tui": "/tui - Voice (speaks the reo)",
            "ngahere": "/ngahere - Auditor (records everything)"
        },
        "tane_mahuta": "Trunk and atua of the forest - holds together all manu",
        "rito": "Heart of the forest - holds mauri and sustains the ngahere",
        "korito_status": korito.get_status()
    }

@app.get("/korito")
async def korito_status():
    """Korito - The heart of the forest status"""
    return korito.get_status()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
