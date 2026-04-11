from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class RecipeBase(BaseModel):
    title: str
    category: str
    ingredients: str  # JSON string
    steps: str        # JSON string
    cook_time: int
    difficulty: str


class RecipeCreate(RecipeBase):
    pass


class RecipeUpdate(BaseModel):
    title: Optional[str] = None
    category: Optional[str] = None
    ingredients: Optional[str] = None
    steps: Optional[str] = None
    cook_time: Optional[int] = None
    difficulty: Optional[str] = None


class RecipeResponse(RecipeBase):
    id: int
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True
