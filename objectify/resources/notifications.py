from __future__ import annotations
from typing import Any, TYPE_CHECKING
if TYPE_CHECKING:
    from objectify.client import ObjectifyClient


class NotificationsResource:
    def __init__(self, client: ObjectifyClient): self._c = client

    def list(self, **p: Any) -> Any: return self._c.get("/v1/auth/notifications", params=p or None)
    def unread_count(self) -> Any: return self._c.get("/v1/auth/notifications/count")
    def mark_read(self, id: str) -> Any: return self._c.patch(f"/v1/auth/notifications/{id}/read")
    def mark_all_read(self) -> Any: return self._c.post("/v1/auth/notifications/read-all")
    def get_preferences(self) -> Any: return self._c.get("/v1/auth/notifications/preferences")
    def update_preferences(self, **d: Any) -> Any: return self._c.patch("/v1/auth/notifications/preferences", json=d)
