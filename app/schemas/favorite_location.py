
from pydantic import BaseModel


class Position(BaseModel):
    lng: float
    lat: float


class Location(BaseModel):
    position: Position
    name: str


class FavoriteLocationBaseSchema(BaseModel):
    title: str
    location: Location
    category_id: int
    owner_id: int


class FavoriteLocationCreateSchema(FavoriteLocationBaseSchema):
    pass


class FavoriteLocationSchema(FavoriteLocationBaseSchema):
    id: int
    category_id: int

    class Config:
        orm_mode = True
