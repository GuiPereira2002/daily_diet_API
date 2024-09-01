from pydantic import BaseModel
from datetime import datetime

class MealBase(BaseModel):
    name: str
    description: str
    date_time: datetime
    in_diet: bool

class MealCreate(MealBase):
    pass

class Meal(MealBase):
    id: int

    class Config:
        orm_mode = True
