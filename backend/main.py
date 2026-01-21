from typing import Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# TODO: add in chromaDB and SQLite and set up connection

app = FastAPI(title="Doc Backend API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def placeholder_response(
    resource: str, action: str, payload: Any | None = None
) -> dict[str, Any]:
    return {
        "resource": resource,
        "action": action,
        "payload": payload,
        "status": "ok",
    }


@app.get("/chat")
def get_chat() -> dict[str, Any]:
    return placeholder_response(
        "chat",
        "get",
        {
            "id": "chat_001",
            "title": "Welcome chat",
            "messages": ["Hello from the backend!"],
        },
    )


@app.post("/chat")
def post_chat() -> dict[str, Any]:
    return placeholder_response(
        "chat",
        "post",
        {
            "id": "chat_002",
            "title": "New chat created",
        },
    )


@app.delete("/chat")
def delete_chat() -> dict[str, Any]:
    return placeholder_response(
        "chat",
        "delete",
        {
            "deleted": True,
            "id": "chat_001",
        },
    )


@app.get("/chat/{chat_id}")
def get_chat_by_id(chat_id: str) -> dict[str, Any]:
    return placeholder_response(
        "chatId",
        "get",
        {
            "id": chat_id,
            "messages": ["Message one", "Message two"],
        },
    )


@app.post("/chat/{chat_id}")
def post_chat_by_id(chat_id: str) -> dict[str, Any]:
    return placeholder_response(
        "chatId",
        "post",
        {
            "id": chat_id,
            "status": "updated",
        },
    )


@app.delete("/chat/{chat_id}")
def delete_chat_by_id(chat_id: str) -> dict[str, Any]:
    return placeholder_response(
        "chatId",
        "delete",
        {
            "deleted": True,
            "id": chat_id,
        },
    )


@app.get("/document")
def get_document() -> dict[str, Any]:
    return placeholder_response(
        "document",
        "get",
        {
            "id": "doc_001",
            "title": "Sample document",
            "content": "This is placeholder content.",
        },
    )


@app.post("/document")
def post_document() -> dict[str, Any]:
    return placeholder_response(
        "document",
        "post",
        {
            "id": "doc_002",
            "title": "Created document",
        },
    )


@app.delete("/document")
def delete_document() -> dict[str, Any]:
    return placeholder_response(
        "document",
        "delete",
        {
            "deleted": True,
            "id": "doc_001",
        },
    )


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
