import uuid
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.models.conversation import Conversation
from app.models.message import Message
from app.services.ai.factory import get_ai_provider
from app.services.analytics import emit_event

router = APIRouter(prefix="/v1/chat", tags=["chat"])

class ChatSendRequest(BaseModel):
    user_id: int
    character_id: str
    conversation_id: str | None = None
    session_id: str | None = None
    message: str

class ChatSendResponse(BaseModel):
    conversation_id: str
    reply: str

@router.post("/send", response_model=ChatSendResponse)
def send(req: ChatSendRequest, db: Session = Depends(get_db)):
    conv_id = req.conversation_id or str(uuid.uuid4())

    conv = db.get(Conversation, conv_id)
    if conv is None:
        conv = Conversation(id=conv_id, user_id=req.user_id, character_id=req.character_id)
        db.add(conv)
        db.commit()

        emit_event(db, "conversation_started", req.user_id, req.session_id, conv_id, {
            "character_id": req.character_id,
            "conversation_type": "new",
        })

    user_msg = Message(conversation_id=conv_id, user_id=req.user_id, role="user", content=req.message, credits_cost=0)
    db.add(user_msg)
    db.commit()

    emit_event(db, "message_sent", req.user_id, req.session_id, conv_id, {
        "message_length": len(req.message),
        "credits_cost": 0
    })

    history = db.query(Message).filter(Message.conversation_id == conv_id).order_by(Message.id.asc()).limit(20).all()
    provider = get_ai_provider()
    reply_text = provider.generate_text(
        [{"role": m.role, "content": m.content} for m in history],
        character_id=req.character_id
    )

    ai_msg = Message(conversation_id=conv_id, user_id=req.user_id, role="assistant", content=reply_text, credits_cost=0)
    db.add(ai_msg)
    db.commit()

    emit_event(db, "ai_response_generated", req.user_id, req.session_id, conv_id, {
        "response_length": len(reply_text),
        "latency_ms": 0
    })

    return ChatSendResponse(conversation_id=conv_id, reply=reply_text)
