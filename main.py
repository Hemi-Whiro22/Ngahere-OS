from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import sys
from pathlib import Path

# Check for Korito (the heart) before starting
sys.path.append(str(Path(__file__).parent / "kaitiaki" / "korito"))
from korito.loader import validate_ngahere_heart


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
from routes.kereru_router import router as kereru_router
from routes.piwakawaka_router import router as piwakawaka_router
from routes.korito_router import router as korito_router
from routes.pukeko_router import router as pukeko_router
from routes.kahu_router import router as kahu_router
from routes.tauhou_router import router as tauhou_router
from routes.riroriro_router import router as riroriro_router
from routes.korora_router import router as korora_router

app = FastAPI(title="Ngahere-OS - Living Forest of Kaitiaki", version="0.1.0")

# Mount all kaitiaki routers
app.include_router(kea_router, prefix="/kea", tags=["Kea - Search"])
app.include_router(ruru_router, prefix="/ruru", tags=["Ruru - Summaries"])
app.include_router(kaka_router, prefix="/kaka", tags=["Kaka - Carver"])
app.include_router(kotare_router, prefix="/kotare", tags=["Kotare - Embeds"])
app.include_router(karearea_router, prefix="/karearea", tags=["Karearea - OCR"])
app.include_router(tui_router, prefix="/tui", tags=["Tui - Voice"])
app.include_router(kereru_router, prefix="/kereru", tags=["Kererū - Gentle Audit"])
app.include_router(piwakawaka_router, prefix="/piwakawaka", tags=["Pīwakawaka - Prompt Dancer"])
app.include_router(korito_router, prefix="/korito", tags=["Korito - Heart of the Forest"])
app.include_router(pukeko_router, prefix="/pukeko", tags=["Pūkeko - Data Guardian"])
app.include_router(kahu_router, prefix="/kahu", tags=["Kahu - Security Sentinel"])
app.include_router(tauhou_router, prefix="/tauhou", tags=["Tauhou - Health Monitor"])
app.include_router(riroriro_router, prefix="/riroriro", tags=["Riroriro - Communication Coordinator"])
app.include_router(korora_router, prefix="/korora", tags=["Kororā - Database Keeper"])

@app.get("/")
async def root():
    """Ngahere-OS - The living forest of kaitiaki guardians"""
    return {
        "name": "Ngahere-OS",
        "description": "Living forest of kaitiaki guardians sustained by Tane Mahuta",
        "version": "0.1.0",
        "kaitiaki": ["kea", "ruru", "kaka", "kotare", "karearea", "tui", "kereru", "piwakawaka", "korito", "pukeko", "kahu", "tauhou", "riroriro", "korora"],
        "endpoints": {
            "kea": "/kea - Searcher (finds things in archives)",
            "ruru": "/ruru - Summariser (brings clarity)", 
            "kaka": "/kaka - Carver (shapes code)",
            "kotare": "/kotare - Embedder (stores knowledge)",
            "karearea": "/karearea - Scanner (sees everything)",
            "tui": "/tui - Voice (speaks the reo)",
            "kereru": "/kereru - Auditor (gentle guardian watching over all)",
            "piwakawaka": "/piwakawaka - Prompt Dancer (zipping around chirping about prompts)",
            "korito": "/korito - Heart of the forest (environment and secrets)",
            "pukeko": "/pukeko - Data Guardian (protects data integrity)",
            "kahu": "/kahu - Security Sentinel (monitors threats)",
            "tauhou": "/tauhou - Health Monitor (system health)",
            "riroriro": "/riroriro - Communication Coordinator (notifications)",
            "korora": "/korora - Database Keeper (manages databases)"
        },
        "tane_mahuta": "Trunk and atua of the forest - holds together all manu",
        "rito": "Heart of the forest - holds mauri and sustains the ngahere"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
