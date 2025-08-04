# -*- coding: utf-8 -*-
"""
HomePage models.
"""
from sqlalchemy import Column, Integer, String

from src.core.db import Base


class HomePage(Base):
    """
    HomePage model.
    """

    __tablename__ = "home_page"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
