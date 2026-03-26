from __future__ import annotations
from typing import Any, TYPE_CHECKING
if TYPE_CHECKING:
    from objectify.client import ObjectifyClient


class ViewsResource:
    def __init__(self, client: ObjectifyClient): self._c = client

    def list(self, type_id: str) -> Any: return self._c.get(f"/v1/object-types/{type_id}/views")
    def create(self, type_id: str, **data: Any) -> Any: return self._c.post(f"/v1/object-types/{type_id}/views", json=data)
    def update(self, type_id: str, view_id: str, **data: Any) -> Any: return self._c.patch(f"/v1/object-types/{type_id}/views/{view_id}", json=data)
    def delete(self, type_id: str, view_id: str) -> Any: return self._c.delete(f"/v1/object-types/{type_id}/views/{view_id}")
