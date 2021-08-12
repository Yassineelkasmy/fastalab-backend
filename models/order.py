from models.restaurant import Restaurant
from models.customer import Customer
from pydantic.main import BaseModel
from models.meal import Meal
from typing import List
from pydantic import  Field
from .model import CoreModel


class Order(CoreModel):
    id:str
    restaurant:Restaurant
    customer:Customer
    meal_id:str
    name:str
    total_amount:float
    total_items:int
    meals:List[Meal]
    longitude:float
    latitude:float
    rating:float
    status:int

status = {
    'queued', #1
    'preparing',#2
    'driving',#3
    'delevired',#4
    'manager-rejected',#5
    'customer-rejected',#6
}
    
    

