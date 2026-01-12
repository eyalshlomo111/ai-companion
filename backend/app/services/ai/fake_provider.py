from typing import List, Dict

class FakeAIProvider:
    def generate_text(self, messages: List[Dict[str, str]], character_id: str) -> str:
        last_user = ""
        for m in reversed(messages):
            if m.get("role") == "user":
                last_user = m.get("content", "")
                break
        return f"(POC) I received: {last_user}"
