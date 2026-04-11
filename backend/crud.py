from sqlalchemy.orm import Session
from models import Recipe
from schemas import RecipeCreate, RecipeUpdate
from typing import Optional, List


def get_recipes(db: Session, skip: int = 0, limit: int = 20, keyword: Optional[str] = None) -> List[Recipe]:
    query = db.query(Recipe)
    if keyword:
        query = query.filter(Recipe.title.contains(keyword))
    return query.order_by(Recipe.id.desc()).offset(skip).limit(limit).all()


def get_recipe(db: Session, recipe_id: int) -> Optional[Recipe]:
    return db.query(Recipe).filter(Recipe.id == recipe_id).first()


def create_recipe(db: Session, recipe: RecipeCreate) -> Recipe:
    db_recipe = Recipe(**recipe.model_dump())
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe


def update_recipe(db: Session, recipe_id: int, recipe: RecipeUpdate) -> Optional[Recipe]:
    db_recipe = get_recipe(db, recipe_id)
    if not db_recipe:
        return None
    update_data = recipe.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_recipe, key, value)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe


def delete_recipe(db: Session, recipe_id: int) -> bool:
    db_recipe = get_recipe(db, recipe_id)
    if not db_recipe:
        return False
    db.delete(db_recipe)
    db.commit()
    return True


def count_recipes(db: Session, keyword: Optional[str] = None) -> int:
    query = db.query(Recipe)
    if keyword:
        query = query.filter(Recipe.title.contains(keyword))
    return query.count()
