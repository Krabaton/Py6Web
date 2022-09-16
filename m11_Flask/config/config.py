import pathlib
from dotenv import dotenv_values
BASE_DIR = pathlib.Path(__file__).parent.parent
config = dotenv_values(".env")


class Config:
    UPLOAD_FOLDER = str(BASE_DIR / 'uploads')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(BASE_DIR / 'data' / 'app.db.sqlite3')
    SECRET_KEY = config['SECRET_KEY']
