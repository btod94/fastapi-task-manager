from fastapi import APIRouter, Depends, HTTPException
from schemas import TaskResponse, TaskCreate
from sqlalchemy.orm import Session
from database import get_db
from services.task_service import get_all_tasks,create_task,get_task_by_id, update_task,delete_task, get_completed_tasks, get_tasks_by_user_id
from services.user_service import get_user_by_id


router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("/", response_model=list[TaskResponse])
def get_tasks(db:Session = Depends(get_db)):
    return get_all_tasks(db)


@router.get("/completed", response_model=list[TaskResponse])
def get_completed_tasks_route(db:Session = Depends(get_db)):
    return get_completed_tasks(db)



@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db:Session = Depends(get_db)):
    task=get_task_by_id(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found") 
    return task

@router.post("/", response_model=TaskResponse)
def create_task_route(task: TaskCreate, db:Session = Depends(get_db)):
    return create_task(db, task)

 
@router.delete("/{task_id}")
def delete_task_route(task_id: int, db:Session = Depends(get_db)):
    task = get_task_by_id(db, task_id)
    if task is None:       
        raise HTTPException(status_code=404, detail="Task not found")
    delete_task(db, task)
    return{"message":"Task deleted"}


@router.put("/{task_id}", response_model=TaskResponse)
def update_task_route(task_id: int, task_data: TaskCreate, db:Session = Depends (get_db)):
    task=get_task_by_id(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    update_task(db, task, task_data)
    return task

@router.get("/by-user/{user_id}", response_model=list[TaskResponse])
def get_task_by_user_id_route(user_id:int, completed:bool|None = None, db:Session=Depends(get_db)):
    user = get_user_by_id(db, user_id)    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return get_tasks_by_user_id(db, user_id, completed)

