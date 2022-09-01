from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from src.db import Base


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(120), nullable=False)
    last_name = Column(String(120), nullable=False)
    email = Column('email', String(100), nullable=False)
    cell_phone = Column('cell_phone', String(100), nullable=False)
    address = Column('address', String(100), nullable=True)
    start_work = Column('start_work', Date, nullable=True)
    students = relationship('Student', secondary='teachers_to_students', back_populates='teachers')


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(120), nullable=False)
    last_name = Column(String(120), nullable=False)
    email = Column('email', String(100), nullable=False)
    cell_phone = Column('cell_phone', String(100), nullable=False)
    address = Column('address', String(100), nullable=True)
    teachers = relationship('Teacher', secondary='teachers_to_students', back_populates='students')
    contacts = relationship('ContactPerson', back_populates='student')


class TeacherStudent(Base):
    __tablename__ = 'teachers_to_students'
    id = Column(Integer, primary_key=True)
    teacher_id = Column('teacher_id', ForeignKey('teachers.id', ondelete='CASCADE'))
    student_id = Column('student_id', ForeignKey('students.id', ondelete='CASCADE'))
    subject = Column('subject', String(100))


class ContactPerson(Base):
    __tablename__ = 'contact_persons'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(120), nullable=False)
    last_name = Column(String(120), nullable=False)
    email = Column('email', String(100), nullable=False)
    cell_phone = Column('cell_phone', String(100), nullable=False)
    address = Column('address', String(100), nullable=True)
    student_id = Column('student_id', ForeignKey('students.id', ondelete='CASCADE'), nullable=False)
    student = relationship('Student', back_populates='contacts')
