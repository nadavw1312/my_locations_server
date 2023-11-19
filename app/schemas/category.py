from pydantic import BaseModel


class CategoryBaseSchema(BaseModel):
    owner_id: int
    title: str


class CategoryCreateSchema(CategoryBaseSchema):
    pass


class CategorySchema(CategoryBaseSchema):
    id: int

    class Config:
        orm_mode = True
