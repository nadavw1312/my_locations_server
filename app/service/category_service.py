

from app.db.crud.category_crud import CategoryCrud
from app.schemas.category import CategoryCreateSchema


class CategoryService():
    @staticmethod
    def create(owner_id: int, title: str):
        category = CategoryCreateSchema(
            owner_id=owner_id, title=title)

        return CategoryCrud.create(category)

    @staticmethod
    def get_by_user_id(owner_id: int):
        list = CategoryCrud.get_by_user_id(owner_id)
        return list
