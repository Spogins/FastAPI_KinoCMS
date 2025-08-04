from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.db import get_session
from src.home.schemas.home import HomePageRead, HomePageUpdate
from src.home.service.home_service import get_homepage, update_homepage

router = APIRouter()

@router.get("/", response_model=HomePageRead)
async def read_homepage(session: AsyncSession = Depends(get_session)):
    homepage = await get_homepage(session)
    if homepage:
        return homepage
    return {"id": 0, "title": "Пусто"}

@router.put("/", response_model=HomePageRead)
async def update_home(data: HomePageUpdate, session: AsyncSession = Depends(get_session)):
    return await update_homepage(session, data)
