from __future__ import annotations
from typing import Any, TYPE_CHECKING
if TYPE_CHECKING:
    from objectify.client import ObjectifyClient


class FilesResource:
    def __init__(self, client: ObjectifyClient): self._c = client

    def get(self, file_id: str) -> Any: return self._c.get(f"/files/{file_id}")
    def update(self, file_id: str, **data: Any) -> Any: return self._c.patch(f"/files/{file_id}", json=data)
    def delete(self, file_id: str) -> Any: return self._c.delete(f"/files/{file_id}")
    def search(self, **params: Any) -> Any: return self._c.get("/files", params=params or None)
    def signed_url(self, file_id: str, expires_in: int | None = None) -> Any: return self._c.get(f"/files/{file_id}/signed-url", params={"expires_in": expires_in} if expires_in else None)
    def list_versions(self, file_id: str) -> Any: return self._c.get(f"/files/{file_id}/versions")
    def get_stats(self) -> Any: return self._c.get("/files/stats")
    def list_folders(self) -> Any: return self._c.get("/files/folders")
    def list_trash(self, **params: Any) -> Any: return self._c.get("/files/trash", params=params or None)
    def restore(self, file_id: str) -> Any: return self._c.post(f"/files/{file_id}/restore")
    def batch_read(self, ids: list[str]) -> Any: return self._c.post("/files/batch/read", json={"ids": ids})
    def batch_delete(self, ids: list[str]) -> Any: return self._c.post("/files/batch/delete", json={"ids": ids})
