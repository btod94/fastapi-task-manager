from fastapi import FastAPI
from database import engine, Base
from routers.tasks import router
from routers.users import router as users_router

app=FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message":"Server Works!"}

app.include_router(router)
app.include_router(users_router)

    