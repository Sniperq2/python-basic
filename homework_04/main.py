import logging
import asyncio

from sqlalchemy.ext.asyncio import AsyncSession

from homework_04.db import async_session
from homework_04.models.user import User

log = logging.getLogger(__name__)


async def create_user(
    session: AsyncSession,
    username: str,
    email: str | None = None,
) -> User:
    user = User(
        username=username,
        email=email,
    )
    session.add(user)
    await session.commit()

    return user


async def main():
    async with async_session() as session:
        user: User = await create_user(
            session,
            "Maria",
        )
        user: User = await create_user(
            session,
            "Jock",
            "jack@example.com",
        )


if __name__ == "__main__":
    asyncio.run(main())
