from sqlalchemy import create_injine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import Column, Integer, String

engine = create_injine("sqlite:///taskmanager.db", echo=True)

class Base(DeclarativeBase):
    pass