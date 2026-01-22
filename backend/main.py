from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from routes.documents import router as document_router
from routes.chats import router as chat_router
from routes.health import router as health_router
from routes.retrieve import router as retrieve_router


# Create the server
app = FastAPI(title="Doc Backend API")

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API routes
app.include_router(retrieve_router)
app.include_router(health_router)
app.include_router(chat_router)
app.include_router(document_router)


# Hot Reload for Backend
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
