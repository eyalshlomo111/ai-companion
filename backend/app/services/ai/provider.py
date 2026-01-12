from typing import Protocol, List, Dict

class AIProvider(Protocol):
    def generate_text(self, messages: List[Dict[str, str]], character_id: str) -> str:
        ...
