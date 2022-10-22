from sqlalchemy import and_
from sqlalchemy.orm import Session

from src.models import Note, User
from src.schemas.notes import NoteBase, NoteUpdate, NoteDone


async def get_all_notes(db: Session, user: User, skip, limit):
    notes = db.query(Note).filter(Note.user == user.id).offset(skip).limit(limit).all()
    return notes


async def get_note(db: Session, note_id: int, user: User):
    note = db.query(Note).filter(and_(Note.id == note_id, Note.user == user.id)).first()
    return note


async def create_note(db: Session, note: NoteBase, user: User):
    new_note = Note(title=note.title, description=note.description, user=user.id)
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note


async def update_note(db: Session, note_id: int, u_note: NoteUpdate, user: User):
    note = db.query(Note).filter(and_(Note.id == note_id, Note.user == user.id)).first()
    if note:
        note.title = u_note.title
        note.description = u_note.description
        note.done = u_note.done
        db.commit()
    return note


async def done_note(db: Session, note_id: int, u_note: NoteDone, user: User):
    note = db.query(Note).filter(and_(Note.id == note_id, Note.user == user.id)).first()
    if note:
        note.done = u_note.done
        db.commit()
    return note


async def delete_note(db: Session, note_id: int, user: User):
    note = db.query(Note).filter(and_(Note.id == note_id, Note.user == user.id)).first()
    if note:
        db.delete(note)
        db.commit()
    return note
