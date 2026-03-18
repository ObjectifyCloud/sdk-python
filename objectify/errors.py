from __future__ import annotations
from typing import Any


class ObjectifyError(Exception):
    def __init__(self, status: int, code: str, message: str, details: Any = None):
        super().__init__(message)
        self.status = status
        self.code = code
        self.details = details

    @classmethod
    def from_response(cls, status: int, body: dict[str, Any] | None) -> ObjectifyError:
        body = body or {}
        code = body.get("code", "unknown_error")
        msg = body.get("message") or body.get("error") or f"HTTP {status}"
        details = body.get("details")
        error_map: dict[int, type[ObjectifyError]] = {
            400: ValidationError, 422: ValidationError,
            401: UnauthorizedError, 403: ForbiddenError,
            404: NotFoundError, 409: ConflictError, 429: RateLimitError,
        }
        cls_type = error_map.get(status, ObjectifyError)
        return cls_type(status, code, msg, details)


class ValidationError(ObjectifyError):
    def __init__(self, status: int = 400, code: str = "validation_error", message: str = "Validation error", details: Any = None):
        super().__init__(status, code, message, details)


class UnauthorizedError(ObjectifyError):
    def __init__(self, status: int = 401, code: str = "unauthorized", message: str = "Unauthorized", details: Any = None):
        super().__init__(status, code, message, details)


class ForbiddenError(ObjectifyError):
    def __init__(self, status: int = 403, code: str = "forbidden", message: str = "Forbidden", details: Any = None):
        super().__init__(status, code, message, details)


class NotFoundError(ObjectifyError):
    def __init__(self, status: int = 404, code: str = "not_found", message: str = "Not found", details: Any = None):
        super().__init__(status, code, message, details)


class ConflictError(ObjectifyError):
    def __init__(self, status: int = 409, code: str = "conflict", message: str = "Conflict", details: Any = None):
        super().__init__(status, code, message, details)


class RateLimitError(ObjectifyError):
    def __init__(self, status: int = 429, code: str = "rate_limit", message: str = "Rate limit exceeded", details: Any = None):
        super().__init__(status, code, message, details)
