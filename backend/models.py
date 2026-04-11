from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.sql import func
from database import Base


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    category = Column(String(50), nullable=False, index=True)
    ingredients = Column(Text, nullable=False)
    steps = Column(Text, nullable=False)
    cook_time = Column(Integer, nullable=False)
    difficulty = Column(String(20), nullable=False)
    image_url = Column(String(500), nullable=True)
    is_favorite = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
