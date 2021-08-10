from typing import Optional
from pydantic import  Field , EmailStr
from .model import Model



class User(Model):
    username:Optional[str]
    email:EmailStr
    phone:str = Field(min_length=10,max_length=20)
    disabled:bool = None
    





# class ClientInDB(User):
#     hashed_password:str
#     firebase_user_id:str
