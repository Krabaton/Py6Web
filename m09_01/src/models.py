from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from src.db import engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    login = Column(String(25), nullable=False, unique=True)
    password = Column(String(25), nullable=False)


class Todo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    title = Column(String(30), nullable=False, index=True)
    description = Column(String(125), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)


Base.metadata.create_all(engine)
Base.metadata.bind = engine
