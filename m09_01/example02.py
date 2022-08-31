from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///sqlalchemy_example.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()


class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('persons.id'))
    person = relationship(Person)


'''
Як об'єкт, що зв'язує стан бази та опис бази, в Python коді виступає Base, саме цей клас відповідає за "магію" 
синхронізації таблиць у базі даних та їх опису в Python класах Person та Address.
'''

Base.metadata.create_all(engine)
Base.metadata.bind = engine

'''
ORM підхід виразніший. Наприклад, додавання нових записів до таблиці – це просто створення нових об'єктів класів Person 
та Address:
'''

new_person = Person(name="Michail")
session.add(new_person)

'''Зверніть увагу, щоб зміни набули чинності, були записані до бази, обов'язково потрібно виконати commit.'''

# session.commit()

new_address = Address(post_code='36065', person=new_person)
session.add(new_address)
session.commit()

'''Щоб отримати дані з бази, можна скористатися методом query:'''

for person in session.query(Person).all():
    print(person.id, person.name)
