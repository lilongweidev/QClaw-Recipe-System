from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


from enum import Enum


class DifficultyEnum(str, Enum):
    easy = "简单"
    medium = "中等"
    hard = "困难"


class RecipeBase(BaseModel):
    title: str
    category: str
    ingredients: str
    steps: str
    cook_time: int = Field(..., gt=0, description="烹饪时间（分钟），必须大于0")
    difficulty: DifficultyEnum


class RecipeCreate(RecipeBase):
    image_url: Optional[str] = None


class RecipeUpdate(BaseModel):
    title: Optional[str] = None
    category: Optional[str] = None
    ingredients: Optional[str] = None
    steps: Optional[str] = None
    cook_time: Optional[int] = Field(None, gt=0)
    difficulty: Optional[DifficultyEnum] = None
    image_url: Optional[str] = None
    is_favorite: Optional[bool] = None


class RecipeResponse(RecipeBase):
    id: int
    image_url: Optional[str] = None
    is_favorite: bool = False
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True
