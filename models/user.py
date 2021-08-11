from typing import Optional
from pydantic import  Field , EmailStr
from .model import CoreModel


class Verification(CoreModel):
    pin_code:str
    expires:str


class User(CoreModel):
    username:Optional[str]
    email:EmailStr
    phone:str = Field(min_length=10,max_length=20)
    disabled:bool = None
    verified:bool = False
    


class UserUpdate(CoreModel):
    username:Optional[str]
    email:Optional[EmailStr]
    phone:Optional[str] = Field(min_length=10,max_length=20)
    disabled:Optional[bool]= None
    verified:Optional[bool] = False
    




class UserInDB(User):
    hashed_password:str
    signup_verification:Optional[Verification]
    forgot_verifcation: Optional[Verification]



# class ClientInDB(User):
#     hashed_password:str
#     firebase_user_id:str
