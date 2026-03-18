from __future__ import annotations
from typing import Any, TYPE_CHECKING
if TYPE_CHECKING:
    from objectify.client import ObjectifyClient


class AssociationsResource:
    def __init__(self, client: ObjectifyClient): self._c = client

    def list(self, type_id: str, object_id: str, **params: Any) -> Any: return self._c.get(f"/objects/{type_id}/{object_id}/associations", params=params or None)
    def create(self, type_id: str, object_id: str, **data: Any) -> Any: return self._c.post(f"/objects/{type_id}/{object_id}/associations", json=data)
    def delete(self, type_id: str, object_id: str, assoc_type: str, to_type_id: str, to_id: str) -> Any: return self._c.delete(f"/objects/{type_id}/{object_id}/associations/{assoc_type}/{to_type_id}/{to_id}")
