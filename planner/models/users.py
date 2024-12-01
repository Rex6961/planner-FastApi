from pydantic import BaseModel, EmailStr
from typing import Optional, List
from planner.models.events import Event

class User(BaseModel):
    email: EmailStr
    password: str
    username: str
    events: Optional[List[Event]] = []

    model_config = {
        "json_schema_extra": {
            "example": {
                    "email": "fastapi@packt.com",
                    "username": "FastPackt",
                    "password": "strong!!!",
                    "events": [],
            }
        }
    }


class UserSingIn(BaseModel):
    email: EmailStr
    password: str

    model_config = {
        "json_schema_extra": {
            "example": {
                    "email": "fastapi@packt.com",
                    "password": "strong!!!",
            }
        }
    }
