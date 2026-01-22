from typing import Any


def placeholder_response(
    resource: str, action: str, payload: Any | None = None
) -> dict[str, Any]:
    return {
        "resource": resource,
        "action": action,
        "payload": payload,
        "status": "ok",
    }
