from typing import Any

from fastapi import APIRouter, File, HTTPException, UploadFile

from pathlib import Path

from routes.placeholders import placeholder_response

router = APIRouter(prefix="/documents", tags=["documents"])

DOCUMENT_DIR = Path("documents")
# make a directory for documents if it doesn't exist
DOCUMENT_DIR.mkdir(exist_ok=True)


# route for single file document
@router.post("/documents/single")
def post_document(file: UploadFile = File(...)):
    """Handles single document being uploaded"""
    # validate the file
    # save the file to the disk (for better file handling, reduce risk to my ram)
    # extract the data needed based on type of file
    # add to the database

    # return message on success
    return placeholder_response(
        "documents",
        "post",
        {
            "id": "doc_002",
            "title": "Created document",
        },
    )


# route for multiple file documents add after main flow works


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
