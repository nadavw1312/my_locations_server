from app.db.crud.base_crud import BaseCrud
from app.db.models.user_model import UserModel
from app.schemas.user_schema import UserCreateSchema, UserSchema
from app.core.singleton import Singleton


class _UserCrud(Singleton, BaseCrud):
    def __init__(self):
        super().__init__(UserModel)

    def create_user(self, user: UserCreateSchema):
        db_user = UserModel(
            username=user.username, password=user.password)
        return self.create(db_user)

    def get_by_username(self, username: str):
        return self.db.query(UserModel).filter(UserModel.username == username).first()

    def get_users(self, skip: int = 0, limit: int = 100):
        return self.db.query(UserModel).offset(skip).limit(limit).all()


UserCrud = _UserCrud()
