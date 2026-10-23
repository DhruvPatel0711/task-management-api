from pydantic import BaseModel, ConfigDict, Field, field_validator

from models import Roles


class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    password: str = Field(min_length=8, max_length=128)

    @field_validator("username")
    @classmethod
    def validate_username(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError("Username cannot be blank")

        if not value.replace("_", "").isalnum():
            raise ValueError(
                "Username can contain only letters, numbers, and underscores"
            )

        return value


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    role: Roles