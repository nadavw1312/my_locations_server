from app.db.crud.base_crud import BaseCrud
from app.db.models.favorite_location import FavoriteLocationModel
from app.schemas.favorite_location import FavoriteLocationCreateSchema, FavoriteLocationSchema


class _FavoriteLocationCrud(BaseCrud):
    def __init__(self):
        super().__init__(FavoriteLocationModel)

    def create(self, favorite_location: FavoriteLocationCreateSchema):
        db_favorite_location = FavoriteLocationModel(
            **favorite_location.model_dump())
        return super().create(db_favorite_location)

    def update(self, favorite_location: FavoriteLocationSchema):
        return super().update(favorite_location)

    def get_by_user_id(self, owner_id: int):
        return self.db.query(FavoriteLocationModel).filter(FavoriteLocationModel.owner_id == owner_id).all()


FavoriteLocationCrud = _FavoriteLocationCrud()
