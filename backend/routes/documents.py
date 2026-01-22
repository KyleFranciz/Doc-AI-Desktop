from typing import Any

from fastapi import APIRouter

from routes.placeholders import placeholder_response

router = APIRouter(prefix="/documents", tags=["documents"])


@router.post("")
def post_document() -> dict[str, Any]:
    return placeholder_response(
        "documents",
        "post",
        {
            "id": "doc_002",
            "title": "Created document",
        },
    )


@router.get("")
def get_documents() -> dict[str, Any]:
    return placeholder_response(
        "documents",
        "get",
        {
            "documents": [
                {
                    "id": "doc_001",
                    "title": "Sample document",
                    "content": "This is placeholder content.",
                }
            ]
        },
    )


@router.delete("/{document_id}")
def delete_document(document_id: str) -> dict[str, Any]:
    return placeholder_response(
        "documents",
        "delete",
        {
            "deleted": True,
            "id": document_id,
        },
    )


@router.post("/{document_id}/reindex")
def post_document_reindex(document_id: str) -> dict[str, Any]:
    return placeholder_response(
        "documents",
        "reindex",
        {
            "id": document_id,
            "status": "queued",
        },
    )
