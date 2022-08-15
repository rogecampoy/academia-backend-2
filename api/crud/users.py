from sqlalchemy.orm import Session

from models.users import CreateUser, PatchUser
from models.database import User


def create_user(db:Session, user:CreateUser):

    db_user = User(
        email = user.email,
        password = user.password
    )

    db.add(db_user)
    db.commit()
    return db_user



def get_user(db:Session, id:str):

    db_user = db.query(User).filter(User.id == id).first()
    return db_user



def get_all_users(db:Session):

    db_users = db.query(User).all()
    return db_users



def update_users(db:Session, id:str, user:PatchUser):

    db_users = get_user(db=db, id=id)
    db_users.email = user.email
    db_users.password = user.password

    db.commit()
    db.refresh(db_users)



def delete_users(id: str, db: Session):

    db.query(User).filter(User.id == id).delete()
    db.commit()