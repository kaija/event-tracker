from fastapi import APIRouter
from app.api.event.api import v1

router = APIRouter()
router.include_router(v1.router, prefix="/event", tags=["event"])
