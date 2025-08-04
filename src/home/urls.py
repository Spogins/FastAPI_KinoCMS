# -*- coding: utf-8 -*-
"""
HomePage urls.
"""
from .endpoints.home import router as home_router

routes = [("", home_router)]
