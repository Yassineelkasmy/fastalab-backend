from bson import ObjectId
from pydantic import BaseModel, Field
from typing import Optional


class PyObjectId(ObjectId):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid objectid')
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')


class Model(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id')
    
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }