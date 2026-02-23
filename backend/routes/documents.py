from typing import Any # will make this more specific later on

# for file uploads
from fastapi import APIRouter, File, UploadFile

# gets the file paths from the apps folder, makes them objects 
from pathlib import Path # can manipulate folders

from rag.documentprocessor import DocumentProcessor # Processes the document (adds to the database and vector_store)
from rag.vector_store import ChromaDocumentVectorStore # controls vector_store
from routes.placeholders import placeholder_response # filler responses to send back
from services.file_validator import FileValidator # validates the files that are sent to the route to make sure they are good to add

# get the router access to make changes
router = APIRouter(prefix="/documents", tags=["documents"])

# get access to the documents folder
DOCUMENT_DIR = Path("documents")
# make a directory for documents if it doesn't exist
DOCUMENT_DIR.mkdir(exist_ok=True)


# processes a single document
@router.post("/single")
async def post_document(file: UploadFile = File(...)):
    """Handles single document being uploaded"""
    # initialize
    validator = FileValidator()
    
    # check if file is valid  (function handles if the file type not valid or too large)
    await validator.validate_file(file)

    # process and extract the text from the file

    # initialize after it validates and size is good
    processor = DocumentProcessor(vectorStore=ChromaDocumentVectorStore())

    # read the uploaded file data


    # process the file
    result = await processor.process_new_document()

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
