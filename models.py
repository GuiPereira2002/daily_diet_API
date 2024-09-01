from sqlalchemy import Column, Integer, String, Boolean, DateTime
from .database import Base

class Meal(Base):
    __tablename__ = "meals"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    date_time = Column(DateTime)
    in_diet = Column(Boolean, default=True)