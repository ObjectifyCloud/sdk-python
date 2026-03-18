from __future__ import annotations
from typing import Any, TYPE_CHECKING
if TYPE_CHECKING:
    from objectify.client import ObjectifyClient


class ReportsResource:
    def __init__(self, client: ObjectifyClient): self._c = client

    def pipeline(self, type_id: str, **d: Any) -> Any: return self._c.post(f"/reports/{type_id}/pipeline", json=d)
    def timeseries(self, type_id: str, **d: Any) -> Any: return self._c.post(f"/reports/{type_id}/timeseries", json=d)
    def leaderboard(self, type_id: str, **d: Any) -> Any: return self._c.post(f"/reports/{type_id}/leaderboard", json=d)
    def funnel(self, type_id: str, **d: Any) -> Any: return self._c.post(f"/reports/{type_id}/funnel", json=d)
