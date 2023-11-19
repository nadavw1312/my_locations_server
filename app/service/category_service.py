

from app.core.singleton_class import SingletonClass
from app.db.crud.category_crud import CategoryCrud
from app.schemas.category import CategoryCreateSchema


class CategoryService(SingletonClass):
    @staticmethod
    def create(owner_id: int, title: str):
        category = CategoryCreateSchema(
            owner_id=owner_id, title=title)

        return CategoryCrud.create(category)

    @staticmethod
    def get_by_user_id(owner_id: int):
        print("get list")
        list = CategoryCrud.get_by_user_id(owner_id)
        print("lis =", list.__str__())
        return list
