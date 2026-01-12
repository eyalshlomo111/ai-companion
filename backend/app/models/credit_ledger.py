from datetime import datetime
from sqlalchemy import DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

class CreditLedgerEntry(Base):
    __tablename__ = "credit_ledger"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True, nullable=False)

    tx_type: Mapped[str] = mapped_column(String(20), nullable=False)  # GRANT/SPEND/EXPIRE/COMPENSATE
    amount: Mapped[int] = mapped_column(Integer, nullable=False)      # always positive number
    source: Mapped[str] = mapped_column(String(50), nullable=False)

    object_type: Mapped[str | None] = mapped_column(String(50), nullable=True)
    object_id: Mapped[str | None] = mapped_column(String(100), nullable=True)

    idempotency_key: Mapped[str] = mapped_column(String(200), unique=True, nullable=False)

    expires_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
