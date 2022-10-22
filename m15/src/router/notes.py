from typing import List

from fastapi import APIRouter, HTTPException, status, Depends, Query, Path
from sqlalchemy.orm import Session

from db.connect import get_db
from src.libs.oauth2 import get_current_user
from src.models import User
from src.repository import notes
from src.schemas.notes import NoteBase, NoteResponse, NoteUpdate, NoteDone

router = APIRouter(prefix="/notes", tags=["notes"])


@router.get("/", response_model=List[NoteResponse])
async def get_all_notes(db: Session = Depends(get_db), skip: int = 0,
                        limit: int = Query(10, ge=10, le=100, description="How you want to get notes"),
                        current_user: User = Depends(get_current_user)):
    all_notes = await notes.get_all_notes(db, current_user, skip, limit)
    return all_notes


@router.get("/{note_id}", response_model=NoteResponse)
async def get_note(note_id: int = Path(ge=1, description="The ID of the note"), db: Session = Depends(get_db),
                   current_user: User = Depends(get_current_user)):
    note = await notes.get_note(db, note_id, current_user)
    print(note)
    if note is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Note with ID {note_id} not found")
    return note


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=NoteResponse)
async def create_note(note: NoteBase, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    note = await notes.create_note(db, note, current_user)
    return note


@router.put("/{note_id}", response_model=NoteResponse)
async def update_note(note_id: int, note: NoteUpdate, db: Session = Depends(get_db),
                      current_user: User = Depends(get_current_user)):
    note = await notes.update_note(db, note_id, note, current_user)
    if note is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Note with ID {note_id} not found")
    return note


@router.patch("/{note_id}", response_model=NoteResponse)
async def done_note(note_id: int, note: NoteDone, db: Session = Depends(get_db),
                    current_user: User = Depends(get_current_user)):
    note = await notes.done_note(db, note_id, note, current_user)
    if note is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Note with ID {note_id} not found")
    return note


@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_note(note_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    note = await notes.delete_note(db, note_id, current_user)
    if note is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Note with ID {note_id} not found")
    return note
