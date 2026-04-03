from fastapi import APIRouter, Depends, HTTPException
from schemas import TaskResponse, TaskCreate
from sqlalchemy.orm import Session
from database import get_db
from models import Task


router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("/", response_model=list[TaskResponse])
def get_tasks(db:Session = Depends(get_db)):
    tasks=db.query(Task).all()
    return tasks


@router.get("/completed", response_model=list[TaskResponse])
def get_completed_tasks(db:Session = Depends(get_db)):
    tasks=db.query(Task).filter(Task.completed==True).all()
    return tasks

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db:Session = Depends(get_db)):
    task=db.query(Task).filter(Task.id==task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found") 
    return task

@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate, db:Session = Depends(get_db)):
    new_task = Task(
        title=task.title,
        completed=task.completed
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task
 

@router.delete("/{task_id}")
def del_task(task_id: int, db:Session = Depends(get_db)):
    task=db.query(Task).filter(Task.id==task_id).first()
    if task is None:       
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return{"message":"Task deleted"}


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_data: TaskCreate, db:Session = Depends (get_db)):
    task=db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    task.title = task_data.title
    task.completed = task_data.completed
    db.commit()
    db.refresh(task)
    return task