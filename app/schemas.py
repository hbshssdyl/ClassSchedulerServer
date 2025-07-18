from pydantic import BaseModel, Field
from enum import Enum

class Role(str, Enum):
    STAFF = "普通员工"
    SENIOR = "高级员工"
    MANAGER = "管理"
    BOSS = "老板"
    ASSISTANT = "一对一助理"

class UserCreate(BaseModel):
    username: str
    password: str
    role: Role = Field(..., description="只能是 普通员工 或 高级员工")

class UserResponse(BaseModel):
    id: int
    username: str
    role: Role

    class Config:
        orm_mode = True
