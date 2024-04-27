from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column


class TimestampModelMixin:
    created_at: Mapped[datetime] = mapped_column(
        default=datetime.now, server_default=func.now()
    )
    updated_at: Mapped[datetime | None] = mapped_column(onupdate=datetime.now)
