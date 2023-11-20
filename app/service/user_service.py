from fastapi import HTTPException
from app.db.crud.user_crud import UserCrud
from app.schemas.user_schema import UserCreateSchema
from app.utils.security import get_hashed_password, verify_password


class UserService:

    @staticmethod
    def create_user(username: str, password: str):
        db_user = UserCrud.get_by_username(username)
        if db_user:
            raise HTTPException(
                status_code=400, detail="Username already registered")

        hashed_password = get_hashed_password(password)
        user = UserCreateSchema(username=username, password=hashed_password)
        return UserCrud.create_user(user)

    @staticmethod
    def authenticate_user(username: str, password: str):
        user = UserCrud.get_by_username(username)
        if not user:
            return None
        if not verify_password(password, user.password):
            return None
        return user

    @staticmethod
    def get_user(username: str):
        user = UserCrud.get_by_username(username)
        return user
