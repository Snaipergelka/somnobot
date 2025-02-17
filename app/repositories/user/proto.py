from typing import Protocol
from uuid import UUID

from app.models.user.db_user import User

__all__ = ("UserRepositoryP",)


class UserRepositoryP(Protocol):
    async def get_user(
        self,
        user_id: UUID,
    ): ...

    async def get_users(
        self,
        _filter,
    ) -> list: ...

    async def create_user(self, user: User) -> UUID: ...

    async def update_user(self) -> None: ...

    async def update_users(self) -> None: ...
