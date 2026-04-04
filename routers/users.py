from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from schemas import UserCreate, UserResponse
from services.user_service import get_all_users, create_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=list[UserResponse])
def get_users(db:Session = Depends(get_db)):
    return get_all_users(db)

@router.post("/", response_model=UserResponse)
def create_user_route(user:UserCreate, db:Session=Depends(get_db)):
    return create_user(db, user)