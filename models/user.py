from typing import Optional,List
from pydantic import  Field
from .model import Model



class User(Model):
    username:str
    email:Optional[str]
    phone:str = Field(min_length=10,max_length=20)
    disabled:bool = None
    

class Restaurant(Model):
    id:str
    address:str
    longitude:float
    latitude:float



class Manager(User):
    first_name:str
    last_name:str
    restaurants:List[Restaurant]




class ManagerInDB(Manager):
    hashed_password:str
    






# class ClientInDB(User):
#     hashed_password:str
#     firebase_user_id:str
