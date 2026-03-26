from __future__ import annotations
from typing import Any, TYPE_CHECKING
if TYPE_CHECKING:
    from objectify.client import ObjectifyClient


class SchemaResource:
    def __init__(self, client: ObjectifyClient): self._c = client

    def list_types(self, **params: Any) -> Any: return self._c.get("/v1/object-types", params=params or None)
    def get_type(self, type_id: str) -> Any: return self._c.get(f"/v1/object-types/{type_id}")
    def create_type(self, name: str) -> Any: return self._c.post("/v1/object-types", json={"name": name})
    def update_type(self, type_id: str, name: str) -> Any: return self._c.patch(f"/v1/object-types/{type_id}", json={"name": name})
    def delete_type(self, type_id: str) -> Any: return self._c.delete(f"/v1/object-types/{type_id}")
    def list_properties(self, type_id: str) -> Any: return self._c.get(f"/v1/object-types/{type_id}/properties")
    def get_property(self, type_id: str, prop_id: str) -> Any: return self._c.get(f"/v1/object-types/{type_id}/properties/{prop_id}")
    def create_property(self, type_id: str, **data: Any) -> Any: return self._c.post(f"/v1/object-types/{type_id}/properties", json=data)
    def update_property(self, type_id: str, prop_id: str, **data: Any) -> Any: return self._c.patch(f"/v1/object-types/{type_id}/properties/{prop_id}", json=data)
    def delete_property(self, type_id: str, prop_id: str) -> Any: return self._c.delete(f"/v1/object-types/{type_id}/properties/{prop_id}")
