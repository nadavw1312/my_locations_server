from sqlalchemy.orm import Session

from .db import models

from . import schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(
        username=user.username, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_categories(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Category).filter(models.Category.owner_id == user_id).offset(skip).limit(limit).all()


def create_user_category(db: Session, category: schemas.CategoryCreate, user_id: int):
    db_item = models.Category(**category.model_dump(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_user_favorite_locations(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.FavoriteLocation).filter(models.FavoriteLocation.owner_id == user_id).offset(skip).limit(limit).all()


def create_user_favorite_locations(db: Session, favorite_location: schemas.FavoriteLocationCreate, user_id: int):
    db_item = models.Category(**favorite_location.model_dump(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
