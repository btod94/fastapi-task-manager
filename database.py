from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#kreiranje baze podataka
DATABASE_URL="sqlite:///./tasks.db"
#kreiranje engine-a 
engine=create_engine(DATABASE_URL, 
connect_args={"check_same_thread": False})
#kreiranje sesije
SessionLocal=sessionmaker(bind=engine)

Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
    

