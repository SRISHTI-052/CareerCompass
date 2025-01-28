# models/user.py

from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    email: str
    job_title: Optional[str] = None
    skills: Optional[list[str]] = []

    class Config:
        orm_mode = True
