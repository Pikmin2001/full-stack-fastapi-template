from fastapi import APIRouter

from app.api.routes import items, login, private, users, utils
from app.core.config import settings

from fastapi import FastAPI
from app.api.routes.outfits import router as outfits_router

app = FastAPI()

app.include_router(outfits_router, prefix="/api")

api_router = APIRouter()
api_router.include_router(login.router)
api_router.include_router(users.router)
api_router.include_router(utils.router)
api_router.include_router(items.router)


if settings.ENVIRONMENT == "local":
    api_router.include_router(private.router)
