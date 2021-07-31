from typing import List

from pydantic import BaseModel
from .user import User
from .restaurant import Restaurant



class Manager(User):
    first_name:str
    last_name:str
    restaurants:List[Restaurant]


class ManagerInDB(Manager):
    hashed_password:str


class NewManager(BaseModel):
    first_name:str
    last_name:str
    email:str
    phone:str
    password:str
