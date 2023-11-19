from fastapi import APIRouter

from app.api.v1 import categories_api, favorite_locations_api, users_api

router = APIRouter(
    prefix="/v1",
)

router.include_router(users_api.router)
router.include_router(categories_api.router)
router.include_router(favorite_locations_api.router)
