import asyncio
from prisma import Prisma


async def main():
    db = Prisma()
    try:
        await db.connect()
        # Lightweight check: count rows in Interaction table
        try:
            _ = await db.interaction.count()
            print("DB connection OK: Interaction table reachable")
        except Exception as table_err:
            print(f"DB connected, but table check failed: {table_err}")
    finally:
        await db.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
