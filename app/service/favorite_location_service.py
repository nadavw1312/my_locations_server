from app.db.crud.faveorite_location_crud import FavoriteLocationCrud
from app.schemas.favorite_location import FavoriteLocationCreateSchema, FavoriteLocationSchema, Location


class FavoriteLocationService:
    @staticmethod
    def create(title: str, location: Location, category_id: int, owner_id: int):
        favorite_location = FavoriteLocationCreateSchema(
            title=title, location=location, category_id=category_id, owner_id=owner_id)

        return FavoriteLocationCrud.create(favorite_location)

    @staticmethod
    def update(item):
        favorite_location = FavoriteLocationSchema(**item)

        return FavoriteLocationCrud.update(favorite_location)

    @staticmethod
    def get_by_user_id(owner_id: int):
        list = FavoriteLocationCrud.get_by_user_id(owner_id)
        return list
