from src import db
from src import models


def get_pictures_user(user_id):
    return db.session.query(models.Picture).where(models.Picture.user_id == user_id).all()