from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import configparser
import pathlib

#  f'postgresql://username:password@domain_name:port/database_name'

file_config = pathlib.Path(__file__).parent.parent.joinpath('config.ini')
config = configparser.ConfigParser()
config.read(file_config)

username = config.get('DB', 'user')
password = config.get('DB', 'password')
db_name = config.get('DB', 'db_name')
domain = config.get('DB', 'domain')

url = f'postgresql://{username}:{password}@{domain}:5432/{db_name}'

engine = create_engine(url, echo=False)
DBSession = sessionmaker(bind=engine)
session = DBSession()
