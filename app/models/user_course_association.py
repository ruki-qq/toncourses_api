from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

if TYPE_CHECKING:
    from .course import Course
    from .user import User


class UserCourseAssociation(Base):
    __tablename__ = "user_course_association"
    __table_args__ = (
        UniqueConstraint("user_id", "course_id", name="idx_unique_user_course"),
    )

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"))
    user: Mapped["User"] = relationship(back_populates="courses")
    course: Mapped["Course"] = relationship(back_populates="users")
