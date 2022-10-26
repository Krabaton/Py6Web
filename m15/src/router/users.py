from typing import List

from fastapi import APIRouter, HTTPException, status, Depends, Query, Path, UploadFile, File
from sqlalchemy.orm import Session
import cloudinary
import cloudinary.uploader
import cloudinary.api
import json

from db.connect import get_db
from src.libs.oauth2 import get_current_user
from src.models import User
from src.repository import users
from src.schemas.users import UserModel, UserResponse
from src.config import config as app_config

router = APIRouter(prefix="/users", tags=["users"])


# @router.get("/", response_model=List[UserResponse])
# async def get_all_users(db: Session = Depends(get_db), skip: int = 0,
#                         limit: int = Query(10, ge=10, le=100, description="How you want to get users")):
#     all_users = await users.get_all_users(db, skip, limit)
#     return all_users
#
#
# @router.get("/{user_id}", response_model=UserResponse)
# async def get_user(user_id: int = Path(ge=1, description="The ID of the user"), db: Session = Depends(get_db)):
#     user = await users.get_user_by_id(db, user_id)
#     if user is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID {user_id} not found")
#     return user


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create_user(user: UserModel, db: Session = Depends(get_db)):
    user = await users.create_user(db, user)
    return user


@router.patch("/avatar", response_model=UserResponse)  #
async def upload_avatar_user(
        file: UploadFile = File(description="A file read as UploadFile"),
        current_user: User = Depends(get_current_user), db: Session = Depends(get_db)
):
    config = cloudinary.config(
        cloud_name=app_config["cloudinary"]["cloud_name"],
        api_key=app_config["cloudinary"]["api_key"],
        api_secret=app_config["cloudinary"]["api_secret"],
        secure=True
    )
    cloudinary.uploader.upload(file.file, public_id=f"TODOApp/{current_user.username}", unique_filename=False,
                               overwrite=True)
    srcURL = cloudinary.CloudinaryImage(f"TODOApp/{current_user.username}").build_url(width=250, height=250,
                                                                                      crop='fill')
    user = await users.update_avatar_user(db, current_user.id, srcURL)
    return user

# @router.put("/{user_id}", response_model=UserResponse)
# async def update_user(user_id: int, user: UserModel, db: Session = Depends(get_db)):
#     user = await users.update_user(db, user_id, user)
#     if user is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID {user_id} not found")
#     return user
#
#
# @router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_user(user_id: int, db: Session = Depends(get_db)):
#     user = await users.delete_user(db, user_id)
#     if user is None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID {user_id} not found")
#     return user
