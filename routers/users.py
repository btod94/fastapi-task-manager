from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import TaskResponse


from database import get_db
from schemas import UserCreate, UserResponse
from services.user_service import get_all_users, create_user, get_user_by_id

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=list[UserResponse])
def get_users(db:Session = Depends(get_db)):
    return get_all_users(db)

@router.post("/", response_model=UserResponse)
def create_user_route(user:UserCreate, db:Session=Depends(get_db)):
    return create_user(db, user)

@router.get("/{user_id}", response_model=UserResponse)
def get_user_by_id_route(user_id: int, db:Session=Depends(get_db)):
    user=get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/{user_id}/tasks", response_model=list[TaskResponse])
def get_user_tasks(user_id:int, db:Session=Depends(get_db)):
    user=get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user.tasks # query shortcut preko relatinshipa