from pydantic import BaseModel


class Login(BaseModel):
    email: str
    password: str
    
class ResponseLogin(BaseModel):
    login: bool
    token:str
    id: str