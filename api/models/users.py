from typing import Optional
from pydantic import BaseModel

class CreateUser(BaseModel):
    email: str
    password: str
    name: str

class PatchUser(BaseModel):
    password: Optional[str] = None
    email: Optional[str] = None