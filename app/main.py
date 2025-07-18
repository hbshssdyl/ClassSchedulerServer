from fastapi import FastAPI
from app.database import Base, engine
from app import models
from app import auth  # 确保你引入了包含路由的模块

app = FastAPI()

# 添加自动建表逻辑
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

# 注册你的路由
app.include_router(auth.router)