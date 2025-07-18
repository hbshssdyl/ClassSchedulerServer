# app/main.py
from fastapi import FastAPI
from app import auth

app = FastAPI()

app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to ClassSchedulerServer!"}
