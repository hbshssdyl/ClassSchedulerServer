# app/auth.py
from fastapi import APIRouter

router = APIRouter()

@router.post("/register")
def register_user(username: str, password: str):
    return {"message": f"User {username} registered."}
