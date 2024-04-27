from datetime import datetime

from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class User(Base):
    username: Mapped[str] = mapped_column(String(16), unique=True)
    email: Mapped[str | None] = mapped_column(String(128), unique=True)
    first_name: Mapped[str] = mapped_column(String(64))
    last_name: Mapped[str] = mapped_column(String(64))
    register_at: Mapped[datetime] = mapped_column(
        default=datetime.now,
        server_default=func.now(),
    )

    def __str__(self):
        return f"{self.__class__.__name__} id={self.id} username={self.username}"

    def __repr__(self):
        return str(self)
