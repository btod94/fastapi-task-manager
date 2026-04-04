from pydantic import BaseModel, field_validator

class TaskCreate(BaseModel):
    title:str
    completed:bool=False
    user_id: int

    @field_validator("title")
    def title_must_not_be_empty(cls, value):
        if not value.strip():
            raise ValueError("Title must not be empty")
        return value

class TaskResponse(BaseModel):
    id: int
    title: str
    completed: bool

    class Config:
        orm_mode=True

class UserCreate(BaseModel):
    username: str

class UserResponse(BaseModel):
    id:int
    username:str

    class Config:
        orm_mode=True


