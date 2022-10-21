from datetime import datetime

from pydantic import BaseModel, Field


class NoteBase(BaseModel):
    title: str = Field(max_length=50)
    description: str = Field(max_length=150, description='The description of the note')


class NoteUpdate(NoteBase):
    done: bool


class NoteDone(BaseModel):
    done: bool


class NoteResponse(NoteBase):
    id: int
    done: bool
    created: datetime

    class Config:
        orm_mode = True
