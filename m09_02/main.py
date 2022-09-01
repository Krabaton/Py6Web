from sqlalchemy.orm import joinedload
from sqlalchemy import and_
from datetime import datetime
from src.db import session
from src.models import Student, Teacher
from faker import Faker
fake = Faker()


def get_students():
        students = session.query(Student).options(joinedload('teachers'), joinedload('contacts')).all()
        for s in students:
            print(vars(s))
            print(f"{[f'id: {t.id} first_name: {t.first_name}' for t in s.teachers]}")
            print(f"{[f'id: {c.id} first_name: {c.first_name}' for c in s.contacts]}")


def get_students_join():
    students = session.query(Student).join('teachers').all()
    for s in students:
        print(vars(s))
        print(f"{[f'id: {t.id} first_name: {t.first_name}' for t in s.teachers]}")


def get_teachers():
    teachers = session.query(Teacher).options(joinedload('students')).filter(and_(
        Teacher.start_work > datetime(year=2015, month=1, day=1),
        Teacher.start_work < datetime(year=2021, month=1, day=1)
    )).all()
    for t in teachers:
        print(vars(t))
        print(f"{[f'id: {s.id} first_name: {s.first_name}' for s in t.students]}")


def add_student():
    teachers = session.query(Teacher).filter(Teacher.id.in_([2, 4])).all()
    student = Student(
            id=10,
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.ascii_free_email(),
            cell_phone=fake.phone_number(),
            address=fake.address(),
            teachers=teachers
        )
    session.add(student)
    session.commit()


def update_student():
    teachers = session.query(Teacher).filter(Teacher.id.in_([1, 2, 3])).all()
    student = session.query(Student).filter(Student.id == 10).one()
    student.teachers = teachers
    session.commit()


def remove_student():
    student = session.query(Student).filter(Student.id == 10).delete()
    session.commit()


if __name__ == '__main__':
    # get_students()
    # get_students_join()
    # get_teachers()
    add_student()
    # update_student()
    # remove_student()
