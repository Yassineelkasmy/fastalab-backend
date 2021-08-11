from typing import Optional,List
from pydantic import  Field
from .model import CoreModel


class Restaurant(CoreModel):
    id:str
    address:str
    longitude:float
    latitude:float


