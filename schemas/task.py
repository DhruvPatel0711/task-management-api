from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, field_validator

from models import Priority, Status


class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    desc: str | None = Field(default=None, max_length=500)
    category: str = Field(min_length=1, max_length=50)
    priority: Priority = Priority.ROUTINE
    deadline: datetime

    @field_validator("title", "category")
    @classmethod
    def validate_not_blank(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError("This field cannot be blank")

        return value

    @field_validator("desc")
    @classmethod
    def validate_description(cls, value: str | None) -> str | None:
        if value is not None:
            value = value.strip()
            return value or None

        return value


class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    desc: str | None
    category: str
    priority: Priority
    status: Status
    deadline: datetime
    toc: datetime
    user_id: int