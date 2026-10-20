import enum
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Enum as SQLenum, VARCHAR, Boolean
from sqlalchemy.orm import relationship 
from database import Base
from sqlalchemy import DateTime


class Status(str, enum.Enum):
    PENDING = "pending"
    ON_GOING = "on going"
    COMPLETED = "completed"

class Priority(str, enum.Enum):
    ROUTINE = "routine"
    ELEVATED = "elevated"
    CRITICAL = "critical"

class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    title = Column(VARCHAR(255), nullable=False)

    desc = Column(Text, nullable=True)

    category = Column(VARCHAR(50), nullable=False)

    priority = Column(SQLenum(Priority, native_enum=False), nullable=False, default=Priority.ROUTINE)

    status = Column(SQLenum(Status, native_enum=False), default=Status.PENDING, nullable=False)

    deadline = Column(DateTime(timezone=True), nullable=False)

    toc = Column(DateTime(timezone=True), nullable=False)

    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    is_deleted = Column(Boolean, default=False, nullable=False)

    owner = relationship("User", back_populates="tasks")



class Roles(str, enum.Enum):
    ADMIN = "admin"
    USER = "user"

class User(Base):

    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

    username = Column(VARCHAR(255), nullable=False, unique=True)

    password = Column(String, nullable=False)

    role = Column(SQLenum(Roles, native_enum=False), nullable=False, default=Roles.USER)

    tasks = relationship("Task", back_populates="owner", cascade="all, delete-orphan")

    is_deleted = Column(Boolean, default=False, nullable=False)