from pydantic import BaseModel, Field, EmailStr


class UserModel(BaseModel):
    username: str = Field(max_length=150)
    email: str = EmailStr()
    password: str = Field(min_length=6, max_length=16)


class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True
