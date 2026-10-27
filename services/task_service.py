from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import Task, Status
from schemas.task import TaskCreate
from datetime import datetime, timezone


async def create_task(
    data: TaskCreate,
    db: AsyncSession,
    user_id: int
):
    new_task = Task(
        title=data.title,
        desc=data.desc,
        category=data.category,
        priority=data.priority,
        status=Status.PENDING,
        deadline=data.deadline,
        toc=datetime.now(timezone.utc),
        user_id=user_id,
    )

    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)

    return new_task


async def get_tasks(
    db: AsyncSession,
    user_id: int
):
    result = await db.execute(
        select(Task).where(
            Task.user_id == user_id,
            Task.is_deleted == False
        )
    )

    return result.scalars().all()


async def get_task(
    db: AsyncSession,
    task_id: int,
    user_id: int
):
    result = await db.execute(
        select(Task).where(
            Task.id == task_id,
            Task.user_id == user_id,
            Task.is_deleted == False
        )
    )

    return result.scalars().first()


async def update_task(
    db: AsyncSession,
    task_id: int,
    user_id: int,
    data: TaskCreate
):
    result = await db.execute(
        select(Task).where(
            Task.id == task_id,
            Task.user_id == user_id,
            Task.is_deleted == False
        )
    )

    task = result.scalars().first()

    if not task:
        return None

    for key, value in data.model_dump().items():
        setattr(task, key, value)

    await db.commit()
    await db.refresh(task)

    return task


async def delete_task(
    db: AsyncSession,
    task_id: int,
    user_id: int
):
    result = await db.execute(
        select(Task).where(
            Task.id == task_id,
            Task.user_id == user_id,
            Task.is_deleted == False
        )
    )

    task = result.scalars().first()

    if not task:
        return None

    task.is_deleted = True

    await db.commit()

    return task


async def restore_task(
    db: AsyncSession,
    task_id: int
):
    task = await db.get(Task, task_id)

    if not task:
        return None

    task.is_deleted = False

    await db.commit()
    await db.refresh(task)

    return task