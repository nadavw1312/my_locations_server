
from sqlalchemy.orm import relationship
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, JSON

from app.db.database import Base


class FavoriteLocationModel(Base):
    __tablename__ = 'favorite_locations'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    location = Column(JSON, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
