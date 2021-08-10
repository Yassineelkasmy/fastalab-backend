from typing import Optional,List
from pydantic import  Field
from .model import Model


class Restaurant(Model):
    id:str
    address:str
    longitude:float
    latitude:float


