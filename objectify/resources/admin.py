from __future__ import annotations
from typing import Any, TYPE_CHECKING
if TYPE_CHECKING:
    from objectify.client import ObjectifyClient


class AdminResource:
    def __init__(self, client: ObjectifyClient):
        self.tenants = AdminTenantsResource(client)
        self.keys = AdminKeysResource(client)
        self.users = AdminUsersResource(client)
        self.webhooks = AdminWebhooksResource(client)
        self.policies = AdminPoliciesResource(client)
        self.forms = AdminFormsResource(client)
        self.automations = AdminAutomationsResource(client)
        self.roles = AdminRolesResource(client)


class AdminTenantsResource:
    def __init__(self, c: ObjectifyClient): self._c = c
    def list(self, **p: Any) -> Any: return self._c.get("/admin/tenants", params=p or None)
    def create(self, **d: Any) -> Any: return self._c.post("/admin/tenants", json=d)
    def get(self, tid: str) -> Any: return self._c.get(f"/admin/tenants/{tid}")
    def delete(self, tid: str) -> Any: return self._c.delete(f"/admin/tenants/{tid}")
    def migrate(self, tid: str, target_shard: str) -> Any: return self._c.post(f"/admin/tenants/{tid}/migrate", json={"target_shard_id": target_shard})
    def set_plan(self, tid: str, plan: str) -> Any: return self._c.put(f"/admin/tenants/{tid}/plan", json={"plan_tier": plan})
    def get_usage(self, tid: str) -> Any: return self._c.get(f"/admin/tenants/{tid}/usage")
    def suspend(self, tid: str, reason: str | None = None) -> Any: return self._c.post(f"/admin/tenants/{tid}/suspend", json={"reason": reason} if reason else None)
    def unsuspend(self, tid: str) -> Any: return self._c.post(f"/admin/tenants/{tid}/unsuspend")
    def analytics(self, tid: str, **p: Any) -> Any: return self._c.get(f"/admin/tenants/{tid}/analytics", params=p or None)
    def sql_query(self, tid: str, query: str) -> Any: return self._c.post(f"/admin/tenants/{tid}/sql", json={"query": query})
    def list_audit_logs(self, tid: str, **p: Any) -> Any: return self._c.get(f"/admin/tenants/{tid}/audit-logs", params=p or None)
    def list_shards(self) -> Any: return self._c.get("/admin/shards")


class AdminKeysResource:
    def __init__(self, c: ObjectifyClient): self._c = c
    def list(self, tid: str) -> Any: return self._c.get(f"/admin/tenants/{tid}/keys")
    def create(self, tid: str, **d: Any) -> Any: return self._c.post(f"/admin/tenants/{tid}/keys", json=d)
    def revoke(self, tid: str, key_id: str) -> Any: return self._c.delete(f"/admin/tenants/{tid}/keys/{key_id}")
    def rotate(self, tid: str, key_id: str) -> Any: return self._c.post(f"/admin/tenants/{tid}/keys/{key_id}/rotate")
    def update(self, tid: str, key_id: str, **d: Any) -> Any: return self._c.patch(f"/admin/tenants/{tid}/keys/{key_id}", json=d)


class AdminUsersResource:
    def __init__(self, c: ObjectifyClient): self._c = c
    def list(self, tid: str, **p: Any) -> Any: return self._c.get(f"/admin/tenants/{tid}/users", params=p or None)
    def create(self, tid: str, **d: Any) -> Any: return self._c.post(f"/admin/tenants/{tid}/users", json=d)
    def get(self, tid: str, uid: str) -> Any: return self._c.get(f"/admin/tenants/{tid}/users/{uid}")
    def update(self, tid: str, uid: str, **d: Any) -> Any: return self._c.patch(f"/admin/tenants/{tid}/users/{uid}", json=d)
    def delete(self, tid: str, uid: str) -> Any: return self._c.delete(f"/admin/tenants/{tid}/users/{uid}")


class AdminWebhooksResource:
    def __init__(self, c: ObjectifyClient): self._c = c
    def list(self, tid: str) -> Any: return self._c.get(f"/admin/tenants/{tid}/webhooks")
    def create(self, tid: str, **d: Any) -> Any: return self._c.post(f"/admin/tenants/{tid}/webhooks", json=d)
    def update(self, tid: str, wid: str, **d: Any) -> Any: return self._c.patch(f"/admin/tenants/{tid}/webhooks/{wid}", json=d)
    def delete(self, tid: str, wid: str) -> Any: return self._c.delete(f"/admin/tenants/{tid}/webhooks/{wid}")
    def test(self, tid: str, wid: str) -> Any: return self._c.post(f"/admin/tenants/{tid}/webhooks/{wid}/test")


class AdminPoliciesResource:
    def __init__(self, c: ObjectifyClient): self._c = c
    def list(self, tid: str, type_id: str) -> Any: return self._c.get(f"/admin/tenants/{tid}/types/{type_id}/policies")
    def create(self, tid: str, type_id: str, **d: Any) -> Any: return self._c.post(f"/admin/tenants/{tid}/types/{type_id}/policies", json=d)
    def update(self, tid: str, type_id: str, pid: str, **d: Any) -> Any: return self._c.patch(f"/admin/tenants/{tid}/types/{type_id}/policies/{pid}", json=d)
    def delete(self, tid: str, type_id: str, pid: str) -> Any: return self._c.delete(f"/admin/tenants/{tid}/types/{type_id}/policies/{pid}")


class AdminFormsResource:
    def __init__(self, c: ObjectifyClient): self._c = c
    def list(self, tid: str) -> Any: return self._c.get(f"/admin/tenants/{tid}/forms")
    def create(self, tid: str, **d: Any) -> Any: return self._c.post(f"/admin/tenants/{tid}/forms", json=d)
    def update(self, tid: str, fid: str, **d: Any) -> Any: return self._c.patch(f"/admin/tenants/{tid}/forms/{fid}", json=d)
    def delete(self, tid: str, fid: str) -> Any: return self._c.delete(f"/admin/tenants/{tid}/forms/{fid}")


class AdminAutomationsResource:
    def __init__(self, c: ObjectifyClient): self._c = c
    def list(self, tid: str) -> Any: return self._c.get(f"/admin/tenants/{tid}/automations")
    def get(self, tid: str, aid: str) -> Any: return self._c.get(f"/admin/tenants/{tid}/automations/{aid}")
    def create(self, tid: str, **d: Any) -> Any: return self._c.post(f"/admin/tenants/{tid}/automations", json=d)
    def update(self, tid: str, aid: str, **d: Any) -> Any: return self._c.patch(f"/admin/tenants/{tid}/automations/{aid}", json=d)
    def delete(self, tid: str, aid: str) -> Any: return self._c.delete(f"/admin/tenants/{tid}/automations/{aid}")
    def trigger(self, tid: str, aid: str) -> Any: return self._c.post(f"/admin/tenants/{tid}/automations/{aid}/trigger")


class AdminRolesResource:
    def __init__(self, c: ObjectifyClient): self._c = c
    def list(self, tid: str) -> Any: return self._c.get(f"/admin/tenants/{tid}/roles")
    def get(self, tid: str, rid: str) -> Any: return self._c.get(f"/admin/tenants/{tid}/roles/{rid}")
    def create(self, tid: str, **d: Any) -> Any: return self._c.post(f"/admin/tenants/{tid}/roles", json=d)
    def update(self, tid: str, rid: str, **d: Any) -> Any: return self._c.patch(f"/admin/tenants/{tid}/roles/{rid}", json=d)
    def delete(self, tid: str, rid: str) -> Any: return self._c.delete(f"/admin/tenants/{tid}/roles/{rid}")
