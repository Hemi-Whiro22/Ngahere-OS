
from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from typing import List, Optional
from mauri.env_loader import load_mauri_env
from kaitiaki.kea import kea_router
from kaitiaki.ruru import ruru_router
from kaitiaki.kaka import kaka_router
from kaitiaki.kotare import kotare_router
from kaitiaki.karearea import karearea_router
from kaitiaki.tui import tui_router
from kaitiaki.ngahere import ngahere_router
# main kaitiaki router
kaitiaki_router = APIRouter()

# mount manu routers (only those that expose endpoints)
kaitiaki_router.include_router(kea_router, prefix="/kea")
kaitiaki_router.include_router(ruru_router, prefix="/ruru")
kaitiaki_router.include_router(kotare_router, prefix="/kotare")
kaitiaki_router.include_router(kaka_router, prefix="/kaka")
kaitiaki_router.include_router(karearea_router, prefix="/karearea")
kaitiaki_router.include_router(tui_router, prefix="/tui")
