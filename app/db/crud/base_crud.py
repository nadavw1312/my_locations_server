from typing import TypeVar
from app.db.database import SessionLocal


T = TypeVar('T')
R = TypeVar('R')


class BaseCrud:

    def __init__(self, model: R):
        self.model = model
        self.db = SessionLocal()

    def create(self, item: T) -> T:
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item

    def update(self, item: T) -> T:
        self.db.query(self.model).filter(
            self.model.id == item.id).update(values=item.model_dump())
        return item

    def get_all(self, skip: int = 0, limit: int = 100):
        return self.db.query(self.model).offset(skip).limit(limit).all()

    def get_by_id(self):
        return self.db.query(self.model).filter(id == self.model.id)
