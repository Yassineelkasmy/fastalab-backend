from typing import List, Optional
from pydantic import  Field
from .model import CoreModel


class Meal(CoreModel):
    id:str
    restaurant_id:str
    name:str
    image:str
    price:float
    hits:int = 0
    orders:int = 0
    delivery_cost:float
    per_km_cost:Optional[float]
    images:List[str]
    longitude:float
    latitude:float
    rating:float
    disabled:bool = None
    expired:bool = None
    
    
class MealInDB(Meal):
    disabled:bool = None
    expired:bool = None

