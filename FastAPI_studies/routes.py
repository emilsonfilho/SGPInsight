from fastapi import FastAPI, Depends, status
from model.user_create import UserCreate
from model.user_response import UserResponse
from model.user import User
from sqlalchemy.orm import Session
from database import get_db

app = FastAPI()

@app.get("/")
def hello():
    return {
        "msg": "Hello, world!"
    }
    
@app.get("/users")
def getUsers():
    return ['Ana', 'Maria', 'João']

@app.get("/users/{user_id}")
def getUser(user_id: int):
    return {
        "id": user_id
    }
    
# Query Parameters
@app.get("/search")
def search(q: str, limit: int = 10):
    return {
        "query": q,
        "limit": limit
    }
    
# Request Body (POST)
@app.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(**user.model_dump())
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user