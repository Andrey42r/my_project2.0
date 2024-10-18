from fastapi import APIRouter
from app.backand.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from task import *


router = APIRouter(prefix="/user", tags=["user"])


@router.get("/")
async def all_users():
    pass


@router.get("/user_id")
async def user_by_id():
    pass


@router.post("/create")
async def create_user():
    pass


@router.put("/update")
async def update_user():
    pass


@router.delete("/delete")
async def delete_user():
    pass


class User(Base):
    __tablename__ = "users", {'extend_existing': True}
    __table_agrs__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(String)
    slug = Column(String, unique=True, index=True)

    tasks = relationship("Task", back_populates='task')


from sqlalchemy.schema import CreateTable
print(CreateTable(User.__table__))
