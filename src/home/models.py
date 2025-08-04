from sqlalchemy import Column, Integer, String
from src.core.db import Base

class HomePage(Base):
    __tablename__ = "home_page"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
