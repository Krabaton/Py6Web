import pathlib

BASE_DIR = pathlib.Path(__file__).parent.parent


class Config:
    UPLOAD_FOLDER = str(BASE_DIR / 'uploads')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(BASE_DIR / 'data' / 'app.db.sqlite3')
