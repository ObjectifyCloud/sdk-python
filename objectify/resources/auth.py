from __future__ import annotations
from typing import Any, TYPE_CHECKING
if TYPE_CHECKING:
    from objectify.client import ObjectifyClient


class AuthResource:
    def __init__(self, client: ObjectifyClient): self._c = client

    def signup(self, email: str, password: str, **extra: Any) -> Any: return self._c.post("/auth/signup", json={"email": email, "password": password, **extra})
    def login(self, email: str, password: str) -> Any: return self._c.post("/auth/login", json={"email": email, "password": password})
    def logout(self) -> Any: return self._c.post("/auth/logout")
    def refresh(self, refresh_token: str) -> Any: return self._c.post("/auth/refresh", json={"refresh_token": refresh_token})
    def get_user(self) -> Any: return self._c.get("/auth/user")
    def update_user(self, **data: Any) -> Any: return self._c.patch("/auth/user", json=data)
    def verify_email(self, token: str) -> Any: return self._c.post("/auth/verify-email", json={"token": token})
    def forgot_password(self, email: str) -> Any: return self._c.post("/auth/forgot-password", json={"email": email})
    def reset_password(self, token: str, password: str) -> Any: return self._c.post("/auth/reset-password", json={"token": token, "password": password})
    def magic_link(self, email: str) -> Any: return self._c.post("/auth/magic-link", json={"email": email})
    def magic_link_verify(self, token: str) -> Any: return self._c.post("/auth/magic-link/verify", json={"token": token})
    def otp_send(self, phone: str) -> Any: return self._c.post("/auth/otp/send", json={"phone": phone})
    def otp_verify(self, phone: str, code: str) -> Any: return self._c.post("/auth/otp/verify", json={"phone": phone, "code": code})
    def anonymous(self) -> Any: return self._c.post("/auth/anonymous")
    def mfa_enroll(self) -> Any: return self._c.post("/auth/mfa/enroll", json={"type": "totp"})
    def mfa_verify(self, ticket: str, code: str) -> Any: return self._c.post("/auth/mfa/verify", json={"ticket": ticket, "code": code})
    def mfa_list(self) -> Any: return self._c.get("/auth/mfa/factors")
    def mfa_unenroll(self, factor_id: str) -> Any: return self._c.post("/auth/mfa/unenroll", json={"factor_id": factor_id})
    def sessions_list(self) -> Any: return self._c.get("/auth/sessions")
    def session_revoke(self, session_id: str) -> Any: return self._c.delete(f"/auth/sessions/{session_id}")
    def passkeys_list(self) -> Any: return self._c.get("/auth/passkeys")
