from pydantic import BaseModel

from app.schemas.category import CategorySchema


class UserBaseSchema(BaseModel):
    username: str


class UserCreateSchema(UserBaseSchema):
    password: str


class UserSchema(UserBaseSchema):
    id: int

    class Config:
        orm_mode = True
