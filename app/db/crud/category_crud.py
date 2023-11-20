from app.db.crud.base_crud import BaseCrud
from app.db.models.category import CategoryModel
from app.schemas.category import CategoryCreateSchema
from app.core.singleton import Singleton


class _CategoryCrud(Singleton, BaseCrud):
    def __init__(self):
        super().__init__(CategoryModel)

    def create(self, category: CategoryCreateSchema):
        db_category = CategoryModel(**category.model_dump())
        return super().create(db_category)

    def get_by_user_id(self, owner_id: int):
        return self.db.query(CategoryModel).filter(CategoryModel.owner_id == owner_id).all()


CategoryCrud = _CategoryCrud()
