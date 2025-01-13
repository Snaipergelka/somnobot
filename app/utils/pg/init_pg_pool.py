from typing import Any

import asyncpg


async def init_pg_pool(
    host: str, port: int, user: str, password: str, database: str, **kwargs: dict[str, Any]
) -> asyncpg.Pool:
    pool = await asyncpg.create_pool(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
        **kwargs,
    )
    return pool
