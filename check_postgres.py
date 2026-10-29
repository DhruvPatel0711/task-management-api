
import asyncio
from sqlalchemy import text
from database import engine


async def main():
    try:
        async with engine.connect() as connection:
            result = await connection.execute(text("SELECT version()"))
            print("PostgreSQL connection successful!")
            print(result.scalar())
    finally:
        await engine.dispose()


asyncio.run(main())
