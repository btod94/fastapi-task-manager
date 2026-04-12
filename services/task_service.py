from sqlalchemy.orm import Session
from models import Task, User
from schemas import TaskCreate
from fastapi import HTTPException

def get_all_tasks(db:Session):
    return db.query(Task).all()

def create_task(db: Session, task: TaskCreate):
    user = db.query(User).filter(User.id == task.user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    new_task=Task (
        title=task.title,
        completed=task.completed,
        user_id = task.user_id
        )
    
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_task_by_id(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

def update_task(db: Session, task: Task, task_data: TaskCreate):
    task.title = task_data.title
    task.completed = task_data.completed
    db.commit()
    db.refresh(task)
    return task

def delete_task(db:Session, task:Task):
    db.delete(task)
    db.commit()

def get_completed_tasks(db:Session):
    task=db.query(Task).filter(Task.completed==True).all()
    return task
 
def get_tasks_by_user_id(db:Session, user_id:int, completed:bool|None=None):
    query = db.query(Task).filter(Task.user_id==user_id)
    if completed is not None:
        query = query.filter(Task.completed==completed)
    
    return query.all()