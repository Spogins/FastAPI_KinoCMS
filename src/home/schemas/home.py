# -*- coding: utf-8 -*-
"""
HomePage schema.
"""
from pydantic import BaseModel


class HomePageUpdate(BaseModel):
    """
    HomePage Update.
    """

    title: str


class HomePageRead(BaseModel):
    """
    HomePage Read.
    """

    id: int
    title: str

    class Config:
        orm_mode = True
