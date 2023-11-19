from fastapi import APIRouter
from starlette.requests import Request

from app.service.category_service import CategoryService


router = APIRouter(
    prefix="/categories",
    tags=["categories"],
)


@router.post("/create")
async def create(request: Request):
    body = await request.json()
    CategoryService.create(body["owner_id"], body["title"])


@router.get("/get_by_user_id/{user_id}")
async def get_by_user_id(user_id):
    return CategoryService.get_by_user_id(int(user_id))
