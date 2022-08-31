from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey
from sqlalchemy import MetaData
from sqlalchemy.sql import select


engine = create_engine('sqlite:///:memory:', echo=True)

metadata = MetaData()

users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('fullname', String)
              )

addresses = Table('addresses', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('user_id', Integer, ForeignKey('users.id')),
                  Column('email_address', String, nullable=False)
                  )

metadata.create_all(engine)


with engine.connect() as conn:
    ins = users.insert().values(name='Anna', fullname='Anna Saifulina')
    print(str(ins))
    result = conn.execute(ins)

    s = select(users)
    result = conn.execute(s)
    for row in result:
        print(row)