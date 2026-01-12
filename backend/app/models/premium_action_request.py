from datetime import datetime
from sqlalchemy import DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

class PremiumActionRequest(Base):
    __tablename__ = "premium_action_requests"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True, nullable=False)

    action_type: Mapped[str] = mapped_column(String(50), nullable=False)
    fulfillment_mode: Mapped[str] = mapped_column(String(30), nullable=False)

    object_type: Mapped[str | None] = mapped_column(String(50), nullable=True)
    object_id: Mapped[str | None] = mapped_column(String(100), nullable=True)

    status: Mapped[str] = mapped_column(String(20), nullable=False)

    base_price: Mapped[int] = mapped_column(Integer, nullable=False)
    final_price: Mapped[int] = mapped_column(Integer, nullable=False)
    discount_applied: Mapped[int] = mapped_column(Integer, default=0, nullable=False)  # store percent * 100 if you want later
    multiplier_applied: Mapped[int] = mapped_column(Integer, default=100, nullable=False) # 120 means 1.2

    idempotency_key: Mapped[str] = mapped_column(String(200), unique=True, nullable=False)

    expires_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
