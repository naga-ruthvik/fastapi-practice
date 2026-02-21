from pydantic import BaseModel
from datetime import date


class UserCreate(BaseModel):
    name: str
    dob: date


class UserRetrieve(BaseModel):
    id: int
    name: str


# class Users(UserRetrieve):
