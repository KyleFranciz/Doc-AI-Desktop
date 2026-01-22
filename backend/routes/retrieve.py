from typing import Any

from fastapi import APIRouter

from routes.placeholders import placeholder_response

router = APIRouter(prefix="/retrieve", tags=["retrieve"])


@router.post("")
def post_retrieve() -> dict[str, Any]:
    return placeholder_response(
        "retrieve",
        "post",
        {
            "status": "ok",
            "results": [],
        },
    )
