from __future__ import annotations
import time
from typing import Any
import httpx
from objectify.errors import ObjectifyError
from objectify.resources.schema import SchemaResource
from objectify.resources.objects import ObjectsResource
from objectify.resources.search import SearchResource
from objectify.resources.files import FilesResource
from objectify.resources.auth import AuthResource
from objectify.resources.admin import AdminResource
from objectify.resources.accounting import AccountingResource
from objectify.resources.ai import AiResource
from objectify.resources.owner import OwnerResource
from objectify.resources.reports import ReportsResource
from objectify.resources.import_export import ImportExportResource
from objectify.resources.notifications import NotificationsResource
from objectify.resources.associations import AssociationsResource
from objectify.resources.views import ViewsResource
from objectify.resources.comments import CommentsResource
from objectify.resources.workflows import WorkflowsResource


class ObjectifyClient:
    def __init__(
        self,
        base_url: str = "https://api.objectify.cloud",
        api_key: str | None = None,
        jwt: str | None = None,
        admin_key: str | None = None,
        timeout: float = 30.0,
        max_retries: int = 2,
    ):
        headers: dict[str, str] = {"Content-Type": "application/json"}
        if admin_key:
            headers["Authorization"] = f"Bearer {admin_key}"
            headers["X-Admin-Key"] = admin_key
        elif jwt:
            headers["Authorization"] = f"Bearer {jwt}"
        elif api_key:
            headers["Authorization"] = f"Bearer {api_key}"

        self._client = httpx.Client(base_url=base_url, headers=headers, timeout=timeout)
        self._max_retries = max_retries

        self.schema = SchemaResource(self)
        self.objects = ObjectsResource(self)
        self.search = SearchResource(self)
        self.files = FilesResource(self)
        self.auth = AuthResource(self)
        self.admin = AdminResource(self)
        self.accounting = AccountingResource(self)
        self.ai = AiResource(self)
        self.owner = OwnerResource(self)
        self.reports = ReportsResource(self)
        self.import_export = ImportExportResource(self)
        self.notifications = NotificationsResource(self)
        self.associations = AssociationsResource(self)
        self.views = ViewsResource(self)
        self.comments = CommentsResource(self)
        self.workflows = WorkflowsResource(self)

    def close(self) -> None:
        self._client.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def request(self, method: str, path: str, *, json: Any = None, params: dict[str, Any] | None = None) -> Any:
        last_err: Exception | None = None
        for attempt in range(self._max_retries + 1):
            try:
                resp = self._client.request(method, path, json=json, params=params)
                if resp.status_code == 204:
                    return None
                body = resp.json() if resp.content else None
                if resp.is_success:
                    return body
                raise ObjectifyError.from_response(resp.status_code, body)
            except ObjectifyError as e:
                if e.status not in (429, 500, 502, 503, 504):
                    raise
                last_err = e
                if attempt < self._max_retries:
                    time.sleep(min(2 ** attempt, 10))
            except httpx.TransportError as e:
                last_err = e
                if attempt < self._max_retries:
                    time.sleep(min(2 ** attempt, 10))
        raise last_err  # type: ignore

    def get(self, path: str, params: dict[str, Any] | None = None) -> Any:
        return self.request("GET", path, params=params)

    def post(self, path: str, json: Any = None, params: dict[str, Any] | None = None) -> Any:
        return self.request("POST", path, json=json, params=params)

    def put(self, path: str, json: Any = None) -> Any:
        return self.request("PUT", path, json=json)

    def patch(self, path: str, json: Any = None) -> Any:
        return self.request("PATCH", path, json=json)

    def delete(self, path: str) -> Any:
        return self.request("DELETE", path)
