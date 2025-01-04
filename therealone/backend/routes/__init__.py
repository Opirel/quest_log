from fastapi import APIRouter
from .routes import router as quests_router

router = APIRouter()
router.include_router(quests_router, prefix="/quests")
