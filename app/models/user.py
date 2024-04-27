from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utils import EmailType

from .base import Base
from .mixins import TimestampModelMixin

if TYPE_CHECKING:
    from .course import Course
    from .user_course_association import UserCourseAssociation


class User(TimestampModelMixin, Base):
    username: Mapped[str] = mapped_column(String(16), unique=True)
    email: Mapped[str | None] = mapped_column(EmailType, unique=True)
    first_name: Mapped[str] = mapped_column(String(64))
    last_name: Mapped[str] = mapped_column(String(64))
    created_courses: Mapped[list["Course"]] = relationship(back_populates="author")
    courses: Mapped[list["UserCourseAssociation"]] = relationship(back_populates="user")

    def __str__(self):
        return f"{self.__class__.__name__} id={self.id} username={self.username}"

    def __repr__(self):
        return str(self)
