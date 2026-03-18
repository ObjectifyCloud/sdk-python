from __future__ import annotations
from typing import Any, TYPE_CHECKING
if TYPE_CHECKING:
    from objectify.client import ObjectifyClient


class AiResource:
    def __init__(self, client: ObjectifyClient):
        self._c = client
        self.conversations = _Conversations(client)

    def models(self) -> Any: return self._c.get("/ai/models")
    def chat(self, messages: list[dict[str, str]], **opts: Any) -> Any: return self._c.post("/ai/chat", json={"messages": messages, **opts})
    def generate(self, prompt: str, **opts: Any) -> Any: return self._c.post("/ai/generate", json={"prompt": prompt, **opts})
    def embeddings(self, texts: list[str], **opts: Any) -> Any: return self._c.post("/ai/embeddings", json={"texts": texts, **opts})
    def search(self, query: str, **opts: Any) -> Any: return self._c.post("/ai/search", json={"query": query, **opts})
    def moderate(self, text: str) -> Any: return self._c.post("/ai/moderate", json={"text": text})
    def auto_tag(self, object_type_id: str, object_id: str) -> Any: return self._c.post("/ai/auto-tag", json={"object_type_id": object_type_id, "object_id": object_id})
    def summarise(self, object_type_id: str, object_id: str) -> Any: return self._c.post("/ai/summarise", json={"object_type_id": object_type_id, "object_id": object_id})


class _Conversations:
    def __init__(self, c: ObjectifyClient): self._c = c
    def list(self, **p: Any) -> Any: return self._c.get("/ai/conversations", params=p or None)
    def get(self, id: str) -> Any: return self._c.get(f"/ai/conversations/{id}")
    def create(self, **d: Any) -> Any: return self._c.post("/ai/conversations", json=d or None)
    def delete(self, id: str) -> Any: return self._c.delete(f"/ai/conversations/{id}")
    def chat(self, id: str, message: str) -> Any: return self._c.post(f"/ai/conversations/{id}/chat", json={"message": message})
