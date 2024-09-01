from sqlalchemy.orm import Session
from . import models, schemas

def get_meal(db:Session, meal_id:int):
    return db.query(models.Meal).filter(models.Meal.id == meal_id).first()

def get_meals(db:Session, skip:int=0, limit: int=10):
    return db.query(models.Meal).offset(skip).limit(limit).all()

def create_meal(db:Session, meal: schemas.MealCreate):
    db_meal = models.Meal(**meal.dict())
    db.add(db_meal)
    db.commit()
    db.refresh(db_meal)
    return db_meal

def delete_meal(db:Session, meal_id:int):
    db_meal = get_meal(db, meal_id)
    if db_meal:
        db.delete(db_meal)
        db.commit()

def upgrade_meal(db: Session, meal_id: int, meal: schemas.MealCreate):
    db_meal = get_meal(db, meal_id)
    if db_meal:
        for key, value in meal.dict().items():
            setattr(db_meal, key, value)
        db.commit()
        db.refresh(db_meal)
        return db_meal