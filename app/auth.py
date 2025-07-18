# app/auth.py
from fastapi import APIRouter
from pydantic import BaseModel

app = APIRouter()

class User(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(user: User):
    return {"message": f"Welcome, {user.username}!"}
