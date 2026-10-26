from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import User, Roles
from schemas.user import UserCreate
from security import hash_password


class UsernameAlreadyExistsError(Exception):
    pass


class AdminUserDeletionError(Exception):
    pass


async def create_user(
    user: UserCreate,
    db: AsyncSession
):
    result = await db.execute(
        select(User).where(User.username == user.username)
    )

    existing_user = result.scalars().first()

    if existing_user:
        raise UsernameAlreadyExistsError()

    new_user = User(
        username=user.username,
        password=hash_password(user.password)
    )

    db.add(new_user)

    await db.commit()
    await db.refresh(new_user)

    return new_user


async def delete_user(
    user_id: int,
    db: AsyncSession
):
    result = await db.execute(
        select(User).where(
            User.id == user_id,
            User.is_deleted == False
        )
    )

    target_user = result.scalars().first()

    if not target_user:
        return None

    if target_user.role == Roles.ADMIN:
        raise AdminUserDeletionError()

    target_user.is_deleted = True

    await db.commit()

    return target_user


async def restore_user(
    user_id: int,
    db: AsyncSession
):
    user = await db.get(User, user_id)

    if not user:
        return None

    user.is_deleted = False

    await db.commit()
    await db.refresh(user)

    return user