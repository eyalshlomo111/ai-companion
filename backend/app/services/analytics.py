import json
import uuid
from datetime import datetime
from sqlalchemy.orm import Session
from app.models.analytics_event import AnalyticsEvent

def emit_event(db: Session, event_name: str, user_id: int | None, session_id: str | None, conversation_id: str | None, payload: dict):
    ev = AnalyticsEvent(
        event_id=str(uuid.uuid4()),
        event_name=event_name,
        ts_utc=datetime.utcnow(),
        user_id=user_id,
        session_id=session_id,
        conversation_id=conversation_id,
        payload_json=json.dumps(payload, ensure_ascii=False),
    )
    db.add(ev)
    db.commit()
