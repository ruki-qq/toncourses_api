from .base import Base
from .mixins import TimestampModelMixin

from sqlalchemy import SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy_utils import URLType


class Course(TimestampModelMixin, Base):
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(Text, default="", server_default="")
    rating: Mapped[float] = mapped_column(SmallInteger, default=0, server_default="0")
    title_pic: Mapped[str | None] = mapped_column(URLType)

    def __str__(self):
        return f"{self.__class__.__name__}, id={self.id}, title={self.title}"

    def __repr__(self):
        return f"{self.id}: {self.title}"
