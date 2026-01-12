from datetime import datetime
from sqlalchemy import DateTime, String, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

class AnalyticsEvent(Base):
    __tablename__ = "analytics_events"

    id: Mapped[int] = mapped_column(primary_key=True)
    event_id: Mapped[str] = mapped_column(String(36), unique=True, nullable=False)
    event_name: Mapped[str] = mapped_column(String(100), index=True, nullable=False)

    ts_utc: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    user_id: Mapped[int | None] = mapped_column(ForeignKey("users.id"), index=True, nullable=True)
    session_id: Mapped[str | None] = mapped_column(String(100), nullable=True)
    conversation_id: Mapped[str | None] = mapped_column(String(100), nullable=True)

    payload_json: Mapped[str] = mapped_column(Text, nullable=False)
