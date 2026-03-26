from __future__ import annotations
from typing import Any, TYPE_CHECKING
if TYPE_CHECKING:
    from objectify.client import ObjectifyClient


class ReportsResource:
    def __init__(self, client: ObjectifyClient): self._c = client

    def pipeline(self, type_id: str, **d: Any) -> Any: return self._c.post("/v1/reports/pipeline", json={"type_id": type_id, **d})
    def timeseries(self, type_id: str, **d: Any) -> Any: return self._c.post("/v1/reports/timeseries", json={"type_id": type_id, **d})
    def leaderboard(self, type_id: str, **d: Any) -> Any: return self._c.post("/v1/reports/leaderboard", json={"type_id": type_id, **d})
    def funnel(self, type_id: str, **d: Any) -> Any: return self._c.post("/v1/reports/funnel", json={"type_id": type_id, **d})
