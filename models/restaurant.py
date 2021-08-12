from typing import Optional,List
from pydantic import  Field
from .model import CoreModel


class Restaurant(CoreModel):
    id:str
    owner_id:str
    name:str
    image:str
    images:List[str]
    address:str
    longitude:float
    latitude:float
    rating:float
    disabled:bool = None
    expired:bool = None



