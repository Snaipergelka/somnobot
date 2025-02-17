import uuid
from dataclasses import dataclass

import asyncpg


@dataclass
class User(asyncpg.Record):
    id: uuid.UUID
    tg_id: int
    name: str
    language: str

