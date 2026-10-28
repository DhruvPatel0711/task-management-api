from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime
from database import engine, Base, get_db
from dotenv import load_dotenv
from schemas.user import UserResponse, UserCreate
from routers.users import router as users_router
from routers.auth import router as auth_router
from routers.tasks import router as task_router
import asyncio

load_dotenv()

app = FastAPI(title="Task Management APIS")

app.include_router(users_router)
app.include_router(auth_router)
app.include_router(task_router)
