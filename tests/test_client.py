import pytest
import httpx
import respx
from objectify import ObjectifyClient, ObjectifyError, UnauthorizedError, RateLimitError, NotFoundError


BASE = "https://test.api"


@pytest.fixture
def client():
    return ObjectifyClient(base_url=BASE, api_key="test-key", max_retries=0)


class TestClient:
    @respx.mock
    def test_auth_header(self, client):
        route = respx.get(f"{BASE}/schema/types").mock(return_value=httpx.Response(200, json={"data": []}))
        client.schema.list_types()
        assert route.calls[0].request.headers["authorization"] == "Bearer test-key"

    @respx.mock
    def test_get_json(self, client):
        respx.get(f"{BASE}/schema/types").mock(return_value=httpx.Response(200, json={"data": [{"name": "test"}]}))
        result = client.schema.list_types()
        assert result["data"][0]["name"] == "test"

    @respx.mock
    def test_post_json(self, client):
        respx.post(f"{BASE}/schema/types").mock(return_value=httpx.Response(200, json={"name": "new"}))
        result = client.schema.create_type("new")
        assert result["name"] == "new"

    @respx.mock
    def test_204_returns_none(self, client):
        respx.delete(f"{BASE}/schema/types/abc").mock(return_value=httpx.Response(204))
        result = client.schema.delete_type("abc")
        assert result is None

    @respx.mock
    def test_401_raises_unauthorized(self, client):
        respx.get(f"{BASE}/schema/types").mock(return_value=httpx.Response(401, json={"code": "unauthorized", "message": "Bad token"}))
        with pytest.raises(UnauthorizedError):
            client.schema.list_types()

    @respx.mock
    def test_404_raises_not_found(self, client):
        respx.get(f"{BASE}/schema/types/xxx").mock(return_value=httpx.Response(404, json={"code": "not_found", "message": "Not found"}))
        with pytest.raises(NotFoundError):
            client.schema.get_type("xxx")

    @respx.mock
    def test_429_raises_rate_limit(self, client):
        respx.get(f"{BASE}/schema/types").mock(return_value=httpx.Response(429, json={"code": "rate_limit", "message": "Too fast"}))
        with pytest.raises(RateLimitError):
            client.schema.list_types()

    @respx.mock
    def test_retry_on_500(self):
        c = ObjectifyClient(base_url=BASE, api_key="k", max_retries=1)
        route = respx.get(f"{BASE}/schema/types")
        route.side_effect = [
            httpx.Response(500, json={"message": "fail"}),
            httpx.Response(200, json={"data": []}),
        ]
        result = c.schema.list_types()
        assert result == {"data": []}
        assert route.call_count == 2


class TestResources:
    def test_all_namespaces(self, client):
        assert client.schema is not None
        assert client.objects is not None
        assert client.search is not None
        assert client.files is not None
        assert client.auth is not None
        assert client.admin is not None
        assert client.accounting is not None
        assert client.ai is not None
        assert client.owner is not None
        assert client.reports is not None
        assert client.import_export is not None
        assert client.notifications is not None

    def test_admin_sub_resources(self, client):
        assert client.admin.tenants is not None
        assert client.admin.keys is not None
        assert client.admin.users is not None
        assert client.admin.webhooks is not None
        assert client.admin.policies is not None
        assert client.admin.forms is not None
        assert client.admin.automations is not None
        assert client.admin.roles is not None
