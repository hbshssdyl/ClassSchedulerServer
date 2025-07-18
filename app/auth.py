from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud, database

router = APIRouter()

@router.post("/register", response_model=schemas.UserResponse)
def register_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    if user.role not in [schemas.Role.STAFF, schemas.Role.SENIOR]:
        raise HTTPException(status_code=403, detail="仅允许注册普通员工或高级员工")
    existing_user = crud.get_user_by_username(db, user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="用户名已存在")
    return crud.create_user(db, user)
