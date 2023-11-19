from fastapi import APIRouter
from starlette.requests import Request

from app.service.favorite_location_service import FavoriteLocationService


router = APIRouter(
    prefix="/favorite_locations",
    tags=["favorite_locations"],
)


@router.post("/create")
async def create(request: Request):
    body = await request.json()
    FavoriteLocationService.create(
        body["title"], body["location"], body["category_id"], body["owner_id"])


@router.put("/update")
async def update(request: Request):
    body = await request.json()
    FavoriteLocationService.update(
        body["item"])


@router.get("/get_user_locations/{user_id}")
async def get_by_user_id(user_id):
    return FavoriteLocationService.get_by_user_id(int(user_id))
