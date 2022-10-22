from typing import List

from fastapi import APIRouter, HTTPException, status, Depends, Query, Path
from sqlalchemy.orm import Session

from db.connect import get_db
from src.repository import users
from src.schemas.users import UserModel, UserResponse

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
