from __future__ import annotations
from typing import Any, TYPE_CHECKING
if TYPE_CHECKING:
    from objectify.client import ObjectifyClient


class WorkflowsResource:
    def __init__(self, client: ObjectifyClient): self._c = client

    def submit(self, type_id: str, object_id: str) -> Any: return self._c.post(f"/v1/objects/{type_id}/{object_id}/submit-for-review")
    def approve(self, type_id: str, object_id: str, **data: Any) -> Any: return self._c.post(f"/v1/objects/{type_id}/{object_id}/approve", json=data or None)
    def reject(self, type_id: str, object_id: str, **data: Any) -> Any: return self._c.post(f"/v1/objects/{type_id}/{object_id}/reject", json=data or None)
    def status(self, type_id: str, object_id: str) -> Any: return self._c.get(f"/v1/objects/{type_id}/{object_id}/workflow-status")
