from pydantic import BaseModel

class HomePageUpdate(BaseModel):
    title: str

class HomePageRead(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True
