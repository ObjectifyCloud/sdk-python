from __future__ import annotations
from typing import Any, TYPE_CHECKING
if TYPE_CHECKING:
    from objectify.client import ObjectifyClient


class SearchResource:
    def __init__(self, client: ObjectifyClient): self._c = client

    def search(self, type_id: str, **params: Any) -> Any: return self._c.post(f"/objects/{type_id}/search", json=params)
    def aggregate(self, type_id: str, **params: Any) -> Any: return self._c.post(f"/objects/{type_id}/aggregate", json=params)
