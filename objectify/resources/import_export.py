from __future__ import annotations
from typing import Any, TYPE_CHECKING
if TYPE_CHECKING:
    from objectify.client import ObjectifyClient


class ImportExportResource:
    def __init__(self, client: ObjectifyClient): self._c = client

    def import_data(self, type_id: str, format: str, data: Any) -> Any: return self._c.post("/v1/data/import", json={"type_id": type_id, "format": format, "data": data})
    def export_data(self, type_id: str, format: str = "json") -> Any: return self._c.post("/v1/data/export", json={"type_id": type_id, "format": format})
    def export_status(self, job_id: str) -> Any: return self._c.get(f"/v1/data/export/{job_id}")
