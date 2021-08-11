from typing import List, Optional

from pydantic.fields import Field
from pydantic.main import BaseModel
from pydantic.networks import EmailStr
from .user import User, UserInDB, UserUpdate
from .restaurant import Restaurant



class Manager(User):
    first_name:str
    last_name:str
    restaurants:Optional[List[Restaurant]] 



class ManagerUpdate(UserUpdate):
    first_name:Optional[str]
    last_name:Optional[str]
    restaurants:Optional[List[Restaurant]] 




class ManagerLogin(BaseModel):
    username:EmailStr
    password:str = Field(...,max_length=50,min_length=8)

    

class ManagerInDB(UserInDB):
    first_name:str
    last_name:str
    restaurants:Optional[List[Restaurant]] 


class ManagerCreate(BaseModel):
    first_name:str
    last_name:str
    email:EmailStr
    phone:str = Field(min_length=10,max_length=20)
    password:str = Field(...,max_length=20,min_length=8)
    

