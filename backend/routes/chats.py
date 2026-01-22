from typing import Any

from fastapi import APIRouter

from routes.placeholders import placeholder_response

# use to log better for errors
# from loguru import logger

router = APIRouter(prefix="/chats", tags=["chats"])


@router.post("")
def post_chat() -> dict[str, Any]:
    return placeholder_response(
        "chats",
        "post",
        {
            "id": "chat_002",
            "title": "New chat created",
        },
    )


@router.get("")
def get_chats() -> dict[str, Any]:
    return placeholder_response(
        "chats",
        "get",
        {
            "chats": [
                {
                    "id": "chat_001",
                    "title": "Welcome chat",
                }
            ]
        },
    )


@router.get("/{chat_id}/messages")
def get_chat_messages(chat_id: str) -> dict[str, Any]:
    return placeholder_response(
        "chatMessages",
        "get",
        {
            "chatId": chat_id,
            "messages": ["Message one", "Message two"],
        },
    )


@router.post("/{chat_id}/messages")
def post_chat_message(chat_id: str) -> dict[str, Any]:
    return placeholder_response(
        "chatMessages",
        "post",
        {
            "chatId": chat_id,
            "status": "created",
        },
    )


@router.put("/{chat_id}/documents")
def put_chat_documents(chat_id: str) -> dict[str, Any]:
    return placeholder_response(
        "chatDocuments",
        "put",
        {
            "chatId": chat_id,
            "documents": ["doc_001"],
        },
    )


@router.get("/{chat_id}/documents")
def get_chat_documents(chat_id: str) -> dict[str, Any]:
    return placeholder_response(
        "chatDocuments",
        "get",
        {
            "chatId": chat_id,
            "documents": ["doc_001"],
        },
    )
