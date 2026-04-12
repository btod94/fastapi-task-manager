from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate

def get_all_users(db:Session):
    return db.query(User).all()

def create_user(db:Session, user:UserCreate):
    new_user=User(username=user.username)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_id(db:Session, user_id:int):
    return db.query(User).filter(User.id==user_id).first()


