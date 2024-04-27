from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, declared_attr, mapped_column, relationship

if TYPE_CHECKING:
    from .user import User


class TimestampModelMixin:
    created_at: Mapped[datetime] = mapped_column(
        default=datetime.now, server_default=func.now()
    )
    updated_at: Mapped[datetime | None] = mapped_column(onupdate=datetime.now)


class UserRelationMixin:
    _user_id_nullable: bool = False
    _user_id_unique: bool = False
    _user_back_populates: str | None = None

    @declared_attr
    def user_id(self) -> Mapped[int]:
        return mapped_column(
            ForeignKey("users.id"),
            nullable=self._user_id_nullable,
            unique=self._user_id_unique,
        )

    @declared_attr
    def user(self) -> Mapped["User"]:
        return relationship(
            back_populates=self._user_back_populates,
        )
