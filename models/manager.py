from typing import List, Optional

from pydantic.fields import Field
from pydantic.main import BaseModel
from pydantic.networks import EmailStr
from .user import User
from .restaurant import Restaurant


class Manager(User):
    first_name:str
    last_name:str
    restaurants:Optional[List[Restaurant]] 

class ManagerLogin(BaseModel):
    username:EmailStr
    password:str = Field(...,max_length=50,min_length=8)

    

class ManagerInDB(User):
    first_name:str
    last_name:str
    hashed_password:str


class ManagerCreate(User):
    first_name:str
    last_name:str
    password:str = Field(...,max_length=20,min_length=8)
