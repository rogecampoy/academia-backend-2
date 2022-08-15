
from secrets import token_hex
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from utils.database import get_db
from models.users import CreateUser, PatchUser
from models.database import User
from crud import users

router = APIRouter(prefix="/users", tags=["users"])

@router.get("")
async def get_all_users(db: Session = Depends(get_db)):

    db_users = users.get_all_users(db)

    return JSONResponse(
        content=[{"email": db_user.email, "password": db_user.password, "user_id": db_user.id} for db_user in db_users],
        status_code=200
    )
@router.get("/{user_id}")
async def get_user(id: int, db:Session = Depends(get_db)):

    db_user = users.get_user(db, id)

    return JSONResponse(
        content={ 
            "email": db_user.email, 
            "password": db_user.password,
            "id": db_user.id,
        },
        status_code=200
    )


@router.post("")
async def create_user(user: CreateUser, db: Session = Depends(get_db)):

    db_user = User(
        email = user.email,
        password = user.password,
        token= token_hex(16)
    )

    db.add(db_user)
    db.commit()
    return JSONResponse(
        content={
            "email": db_user.email,
            "password": db_user.password,
            "id": db_user.id,
        },
        status_code=201
    )


@router.patch("")
async def update_user(id: str, user: PatchUser, db: Session = Depends(get_db)):

    users.update_users(db=db, user=user, id=id)

    return JSONResponse(
        content={
            "status": "SUCCESS",
            "message": "User successfully updated",
            "email": user.email,
            "password": user.password,
            "id": id,
        },
        status_code=201
    )

@router.delete("")
def delete_user(id: str, db: Session = Depends(get_db)):

    deleted_user = users.delete_users(db=db,id=id)

    return JSONResponse(
        content={"status": "SUCCESS", "message": f"User {deleted_user} successfully deleted"},
        status_code=200,
    )