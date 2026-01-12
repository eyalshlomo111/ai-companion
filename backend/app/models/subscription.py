from datetime import datetime
from sqlalchemy import DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.core.enums import SubscriptionStatus

class Subscription(Base):
    __tablename__ = "subscriptions"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True, nullable=False)

    status: Mapped[str] = mapped_column(String(20), default=SubscriptionStatus.ACTIVE.value, nullable=False)
    plan_id: Mapped[str] = mapped_column(String(50), default="POC_SINGLE_PLAN", nullable=False)

    started_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    ends_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
