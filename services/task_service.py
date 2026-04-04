from sqlalchemy.orm import Session
from models import Task
from schemas import TaskCreate

def get_all_tasks(db:Session):
    return db.query(Task).all()

def create_task(db: Session, task: TaskCreate):
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
 
