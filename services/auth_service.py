from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from security import verify_password, create_access_token


async def authenticate_user(
    username: str,
    password: str,
    db: AsyncSession
):
    result = await db.execute(
        select(User).where(
            User.username == username,
            User.is_deleted == False
        )
    )

    user = result.scalars().first()

    if not user:
        return None

    if not verify_password(password, user.password):
        return None

    return user


def generate_access_token(user: User):
    return create_access_token({
        "sub": str(user.id),
        "role": user.role.value
    })