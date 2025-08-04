from fastapi import APIRouter
from src.home.urls import routes as home_routes

router = APIRouter()

for prefix, r in home_routes:
    prefix = prefix.rstrip('/')  # на всякий случай
    router.include_router(r, prefix=prefix)