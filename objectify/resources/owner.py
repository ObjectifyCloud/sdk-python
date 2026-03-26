from __future__ import annotations
from typing import Any, TYPE_CHECKING
if TYPE_CHECKING:
    from objectify.client import ObjectifyClient


class OwnerResource:
    def __init__(self, client: ObjectifyClient): self._c = client

    def login(self, email: str, password: str) -> Any: return self._c.post("/owner/login", json={"email": email, "password": password})
    def signup(self, email: str, password: str, **extra: Any) -> Any: return self._c.post("/owner/signup", json={"email": email, "password": password, **extra})
    def get_profile(self) -> Any: return self._c.get("/owner/profile")
    def update_profile(self, **d: Any) -> Any: return self._c.patch("/owner/profile", json=d)
    def change_password(self, current: str, new: str) -> Any: return self._c.post("/owner/change-password", json={"current_password": current, "new_password": new})
    def forgot_password(self, email: str) -> Any: return self._c.post("/owner/forgot-password", json={"email": email})
    def reset_password(self, token: str, password: str) -> Any: return self._c.post("/owner/reset-password", json={"token": token, "password": password})
    def list_tenants(self) -> Any: return self._c.get("/owner/tenants")
    def create_tenant(self, name: str, **d: Any) -> Any: return self._c.post("/owner/tenants", json={"name": name, **d})
    def switch_tenant(self, tenant_id: str) -> Any: return self._c.post("/owner/switch-tenant", json={"tenant_id": tenant_id})
    def mfa_enroll(self) -> Any: return self._c.post("/owner/mfa/enroll", json={"type": "totp"})
    def mfa_verify(self, code: str) -> Any: return self._c.post("/owner/mfa/verify", json={"code": code})
    def mfa_list(self) -> Any: return self._c.get("/owner/mfa/factors")
