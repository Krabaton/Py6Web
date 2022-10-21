from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.sqltypes import DateTime

from db.connect import Base


class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(String(150), nullable=False)
    done = Column(Boolean, default=False)
    created = Column(DateTime, default=datetime.now())
