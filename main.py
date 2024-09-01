from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.post("/meals/", response_model=schemas.Meal)
def create_meal(meal: schemas.MealCreate, db: Session = Depends(database.get_db)):
    return crud.create_meal(db=db, meal=meal)

@app.get("/meals/", response_model=list[schemas.Meal])
def read_meals(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.get_meals(db, skip=skip, limit=limit)

@app.get("/meals/{meal_id}", response_model=schemas.Meal)
def read_meal(meal_id: int, db: Session = Depends(database.get_db)):
    db_meal = crud.get_meal(db, meal_id=meal_id)
    if db_meal is None:
        raise HTTPException(status_code=404, detail="Meal not found")
    return db_meal

@app.delete("/meals/{meal_id}")
def delete_meal(meal_id: int, db: Session = Depends(database.get_db)):
    crud.delete_meal(db, meal_id)
    return {"detail": "Meal deleted"}

@app.put("/meals/{meal_id}", response_model=schemas.Meal)
def update_meal(meal_id: int, meal: schemas.MealCreate, db: Session = Depends(database.get_db)):
    return crud.update_meal(db, meal_id, meal)
