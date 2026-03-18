from __future__ import annotations
from typing import Any, TYPE_CHECKING
if TYPE_CHECKING:
    from objectify.client import ObjectifyClient


class ImportExportResource:
    def __init__(self, client: ObjectifyClient): self._c = client

    def import_data(self, type_id: str, format: str, data: Any) -> Any: return self._c.post(f"/objects/{type_id}/import", json={"format": format, "data": data})
    def export_data(self, type_id: str, format: str = "json") -> Any: return self._c.post(f"/objects/{type_id}/export", params={"format": format})
    def export_status(self, job_id: str) -> Any: return self._c.get(f"/exports/{job_id}")
