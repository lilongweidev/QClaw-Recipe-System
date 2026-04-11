from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import Optional
from database import get_db
from schemas import RecipeCreate, RecipeUpdate, RecipeResponse
from models import Recipe
import crud

router = APIRouter(prefix="/api/recipes", tags=["recipes"])


@router.get("", response_model=dict)
def list_recipes(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    keyword: Optional[str] = None,
    category: Optional[str] = None,
    sort: Optional[str] = "newest",
    favorites_only: bool = Query(False),
    db: Session = Depends(get_db),
):
    """获取菜谱列表，支持分页、搜索、分类筛选、排序、收藏筛选"""
    recipes = crud.get_recipes(db, skip=skip, limit=limit, keyword=keyword,
                               category=category, sort=sort, favorites_only=favorites_only)
    total = crud.count_recipes(db, keyword=keyword, category=category, favorites_only=favorites_only)
    return {"items": [RecipeResponse.model_validate(r) for r in recipes], "total": total}


@router.get("/categories", response_model=dict)
def list_categories(db: Session = Depends(get_db)):
    """获取所有分类及其数量"""
    results = db.query(Recipe.category, func.count(Recipe.id).label("count")).group_by(Recipe.category).all()
    return {"categories": [{"name": r[0], "count": r[1]} for r in results]}


@router.get("/{recipe_id}", response_model=RecipeResponse)
def get_recipe(recipe_id: int, db: Session = Depends(get_db)):
    """获取单个菜谱详情"""
    recipe = crud.get_recipe(db, recipe_id)
    if not recipe:
        raise HTTPException(status_code=404, detail="菜谱不存在")
    return RecipeResponse.model_validate(recipe)


@router.post("", response_model=RecipeResponse, status_code=201)
def create_recipe(recipe: RecipeCreate, db: Session = Depends(get_db)):
    """新增菜谱"""
    return RecipeResponse.model_validate(crud.create_recipe(db, recipe))


@router.put("/{recipe_id}", response_model=RecipeResponse)
def update_recipe(recipe_id: int, recipe: RecipeUpdate, db: Session = Depends(get_db)):
    """更新菜谱"""
    updated = crud.update_recipe(db, recipe_id, recipe)
    if not updated:
        raise HTTPException(status_code=404, detail="菜谱不存在")
    return RecipeResponse.model_validate(updated)


@router.patch("/{recipe_id}/favorite", response_model=RecipeResponse)
def toggle_favorite(recipe_id: int, db: Session = Depends(get_db)):
    """切换收藏状态"""
    recipe = crud.get_recipe(db, recipe_id)
    if not recipe:
        raise HTTPException(status_code=404, detail="菜谱不存在")
    recipe.is_favorite = not recipe.is_favorite
    db.commit()
    db.refresh(recipe)
    return RecipeResponse.model_validate(recipe)


@router.delete("/{recipe_id}", status_code=204)
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    """删除菜谱"""
    success = crud.delete_recipe(db, recipe_id)
    if not success:
        raise HTTPException(status_code=404, detail="菜谱不存在")
    return None
