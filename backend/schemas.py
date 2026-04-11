from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class RecipeBase(BaseModel):
    title: str
    category: str
    ingredients: str
    steps: str
    cook_time: int
    difficulty: str


class RecipeCreate(RecipeBase):
    image_url: Optional[str] = None


class RecipeUpdate(BaseModel):
    title: Optional[str] = None
    category: Optional[str] = None
    ingredients: Optional[str] = None
    steps: Optional[str] = None
    cook_time: Optional[int] = None
    difficulty: Optional[str] = None
    image_url: Optional[str] = None
    is_favorite: Optional[bool] = None


class RecipeResponse(RecipeBase):
    id: int
    image_url: Optional[str] = None
    is_favorite: bool = False
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True
