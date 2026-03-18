from __future__ import annotations
import asyncio
from typing import Any
import httpx
from objectify.errors import ObjectifyError


class AsyncObjectifyClient:
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

        self._client = httpx.AsyncClient(base_url=base_url, headers=headers, timeout=timeout)
        self._max_retries = max_retries

    async def close(self) -> None:
        await self._client.aclose()

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        await self.close()

    async def request(self, method: str, path: str, *, json: Any = None, params: dict[str, Any] | None = None) -> Any:
        last_err: Exception | None = None
        for attempt in range(self._max_retries + 1):
            try:
                resp = await self._client.request(method, path, json=json, params=params)
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
                    await asyncio.sleep(min(2 ** attempt, 10))
            except httpx.TransportError as e:
                last_err = e
                if attempt < self._max_retries:
                    await asyncio.sleep(min(2 ** attempt, 10))
        raise last_err  # type: ignore

    async def get(self, path: str, params: dict[str, Any] | None = None) -> Any:
        return await self.request("GET", path, params=params)

    async def post(self, path: str, json: Any = None, params: dict[str, Any] | None = None) -> Any:
        return await self.request("POST", path, json=json, params=params)

    async def put(self, path: str, json: Any = None) -> Any:
        return await self.request("PUT", path, json=json)

    async def patch(self, path: str, json: Any = None) -> Any:
        return await self.request("PATCH", path, json=json)

    async def delete(self, path: str) -> Any:
        return await self.request("DELETE", path)
