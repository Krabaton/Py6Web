from sqlalchemy.orm import Session
from libgravatar import Gravatar

from src.models import User
from src.schemas.users import UserModel
from src.libs.hash import Hash


async def get_all_users(db: Session, skip, limit):
    users = db.query(User).offset(skip).limit(limit).all()
    return users


async def get_user_by_id(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    return user


async def get_user_by_email(db: Session, email: str) -> User:
    user = db.query(User).filter(User.email == email).first()
    return user


async def create_user(db: Session, user: UserModel):
    avatar = None
    try:
        g = Gravatar(user.email)
        avatar = g.get_image()
    except Exception as err:
        print(err)

    new_user = User(username=user.username, email=user.email, password=Hash.get_password_hash(user.password),
                    avatar=avatar)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


async def update_user(db: Session, user_id: int, u_user: UserModel):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        await user.update(username=u_user.username, email=u_user.email,
                          password=Hash.get_password_hash(u_user.password)).apply()
    return user


async def update_avatar_user(db: Session, user_id: int, avatar_url: str):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.avatar = avatar_url
        db.commit()
    return user


async def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        await user.delete()
    return user
