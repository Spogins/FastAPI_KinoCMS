# -*- coding: utf-8 -*-
"""
HomePage service.
"""
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from src.home.models import HomePage
from src.home.schemas.home import HomePageUpdate


async def get_homepage(session: AsyncSession) -> HomePage | None:
    """
    Get homepage.
    """
    result = await session.execute(select(HomePage))
    return result.scalar_one_or_none()


async def update_homepage(session: AsyncSession, data: HomePageUpdate) -> HomePage:
    """
    Update homepage.
    """
    homepage = await get_homepage(session)
    if homepage is None:
        homepage = HomePage(title=data.title)
        session.add(homepage)
    else:
        homepage.title = data.title
    await session.commit()
    await session.refresh(homepage)
    return homepage
