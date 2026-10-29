import asyncio

from sqlalchemy import select
from database import AsyncSessionLocal
from models import User, Roles
from security import hash_password, verify_password


async def main():
    async with AsyncSessionLocal() as db:
        result = await db.execute(
            select(User).where(User.username == "testadmin")
        )
        user = result.scalars().first()

        if not user:
            user = User(
                username="testadmin",
                password=hash_password("Admin123"),
                role=Roles.ADMIN,
                is_deleted=False,
            )
            db.add(user)
            await db.commit()
            await db.refresh(user)
            print("Admin created successfully.")
        else:
            print("Admin already exists.")

        print("Username:", user.username)
        print("Role:", user.role)
        print("Password valid:", verify_password("Admin123", user.password))


asyncio.run(main())