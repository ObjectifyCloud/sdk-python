from __future__ import annotations
from typing import Any, TYPE_CHECKING
if TYPE_CHECKING:
    from objectify.client import ObjectifyClient


class ObjectsResource:
    def __init__(self, client: ObjectifyClient): self._c = client

    def list(self, type_id: str, **params: Any) -> Any: return self._c.get(f"/v1/objects/{type_id}/list", params=params or None)
    def get(self, type_id: str, object_id: str) -> Any: return self._c.get(f"/v1/objects/{type_id}/{object_id}")
    def create(self, type_id: str, properties: dict[str, Any]) -> Any: return self._c.post(f"/v1/objects/{type_id}", json={"properties": properties})
    def update(self, type_id: str, object_id: str, properties: dict[str, Any]) -> Any: return self._c.patch(f"/v1/objects/{type_id}/{object_id}", json={"properties": properties})
    def delete(self, type_id: str, object_id: str) -> Any: return self._c.delete(f"/v1/objects/{type_id}/{object_id}")
    def batch_create(self, type_id: str, items: list[dict[str, Any]]) -> Any: return self._c.post(f"/v1/objects/{type_id}/batch/create", json={"items": items})
    def batch_update(self, type_id: str, items: list[dict[str, Any]]) -> Any: return self._c.post(f"/v1/objects/{type_id}/batch/update", json={"items": items})
    def batch_read(self, type_id: str, ids: list[str]) -> Any: return self._c.post(f"/v1/objects/{type_id}/batch/read", json={"ids": ids})
    def list_trash(self, type_id: str, **params: Any) -> Any: return self._c.get(f"/v1/objects/{type_id}/trash", params=params or None)
    def restore(self, type_id: str, object_id: str) -> Any: return self._c.post(f"/v1/objects/{type_id}/{object_id}/restore")
    def list_versions(self, type_id: str, object_id: str) -> Any: return self._c.get(f"/v1/objects/{type_id}/{object_id}/versions")
