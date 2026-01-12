from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

class Conversation(Base):
    __tablename__ = "conversations"

    id: Mapped[str] = mapped_column(String(36), primary_key=True)  # uuid string
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True, nullable=False)
    character_id: Mapped[str] = mapped_column(String(36), nullable=False)  # keep as string for POC
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
