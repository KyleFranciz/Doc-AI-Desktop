from typing import Any

from fastapi import APIRouter, File, UploadFile

from pathlib import Path

from rag.documentprocessor import DocumentProcessor
from rag.vector_store import ChromaDocumentVectorStore
from routes.placeholders import placeholder_response
from services.file_validator import FileValidator

# get the router access to make changes
router = APIRouter(prefix="/documents", tags=["documents"])

# get access to the documents folder
DOCUMENT_DIR = Path("documents")
# make a directory for documents if it doesn't exist
DOCUMENT_DIR.mkdir(exist_ok=True)


# route for single file document
@router.post("/single")
async def post_document(file: UploadFile = File(...)):
    """Handles single document being uploaded"""
    validator = FileValidator()
    # validate the file
    await validator.validate_file(file)
    #
    processor = DocumentProcessor(vectorStore=ChromaDocumentVectorStore())
    result = await processor.process_new_document(file)

    # return message on success to test route
    return {"status": "ok", "doc_id": result.doc_id}  # result.id


# route for multiple file documents add after main flow works


# route to get document data
@router.get("")
def get_documents() -> dict[str, Any]:
    # dummy response to test route
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


# route to delete document
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


# route to reindex document that was previously add
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
