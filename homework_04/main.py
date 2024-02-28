import logging
import asyncio
from typing import List

from aiohttp import ClientSession

from sqlalchemy.ext.asyncio import AsyncSession

from homework_04.db import async_session
from homework_04.jsonplaceholder_requests import USERS_DATA_URL, POSTS_DATA_URL
from homework_04.models import User, Post

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


async def create_posts(
        session: AsyncSession,
        user: User,
        *posts: dict,
) -> list[Post]:
    posts = [Post(title=post["title"], body=post["body"], user_id=user.id) for post in posts]
    session.add_all(posts)
    await session.commit()

    return posts


async def fetch_api(url: str) -> List[dict]:
    async with ClientSession() as session:
        async with session.get(url) as response:
            data: List = await response.json()
            return data


async def main():
    user_fetch, posts_fetch = asyncio.gather(
        fetch_api(USERS_DATA_URL),
        fetch_api(POSTS_DATA_URL)
    )

    async with async_session() as session:
        for userItem in user_fetch:
            user: User = await create_user(
                session,
                userItem["username"],
                userItem["email"]
            )
            for postItem in posts_fetch:
                await create_posts(
                    session,
                    userItem["username"],
                    postItem
                )


if __name__ == "__main__":
    asyncio.run(main())
