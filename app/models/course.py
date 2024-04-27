from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, SmallInteger, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utils import URLType

from .base import Base
from .mixins import TimestampModelMixin

if TYPE_CHECKING:
    from .user import User
    from .user_course_association import UserCourseAssociation


class Course(TimestampModelMixin, Base):
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(Text, default="", server_default="")
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    author: Mapped["User"] = relationship(back_populates="created_courses")
    users: Mapped[list["UserCourseAssociation"]] = relationship(back_populates="user")
    rating: Mapped[float] = mapped_column(SmallInteger, default=0, server_default="0")
    title_pic: Mapped[str | None] = mapped_column(URLType)

    def __str__(self):
        return f"{self.__class__.__name__}, id={self.id}, title={self.title}"

    def __repr__(self):
        return f"{self.id}: {self.title}"
