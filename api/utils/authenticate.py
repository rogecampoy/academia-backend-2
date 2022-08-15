from fastapi import Header
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.database import User
from utils.exceptions import Unauthorized
from .database import db_engine



def authenticate(token: str = Header(...)):
    engine = create_engine(db_engine())

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    db = SessionLocal()

    token = db.query(User).filter(User.token == token).first()

    if token is None:
        raise Unauthorized("You are not allowed to access this resource")
