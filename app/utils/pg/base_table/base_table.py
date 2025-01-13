import asyncpg

from app.utils.singleton import Singleton


class BaseTable(metaclass=Singleton):
    __slots__ = ("pg_pool", )

    def __init__(self, pg_pool: asyncpg.Pool):
        self.pg_pool = pg_pool

    @property
    def table(self) -> str:
        raise NotImplementedError("Override table() to set table name")

