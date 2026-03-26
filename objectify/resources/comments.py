from __future__ import annotations
from typing import Any, TYPE_CHECKING
if TYPE_CHECKING:
    from objectify.client import ObjectifyClient


class CommentsResource:
    def __init__(self, client: ObjectifyClient): self._c = client

    def list(self, type_id: str, object_id: str, **params: Any) -> Any: return self._c.get(f"/v1/objects/{type_id}/{object_id}/comments", params=params or None)
    def create(self, type_id: str, object_id: str, body: str) -> Any: return self._c.post(f"/v1/objects/{type_id}/{object_id}/comments", json={"body": body})
    def update(self, type_id: str, object_id: str, comment_id: str, body: str) -> Any: return self._c.patch(f"/v1/objects/{type_id}/{object_id}/comments/{comment_id}", json={"body": body})
    def delete(self, type_id: str, object_id: str, comment_id: str) -> Any: return self._c.delete(f"/v1/objects/{type_id}/{object_id}/comments/{comment_id}")
