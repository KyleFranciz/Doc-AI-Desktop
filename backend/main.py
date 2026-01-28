from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from routes.documents import router as document_router
from routes.chats import router as chat_router
from routes.health import router as health_router
from routes.retrieve import router as retrieve_router
from db.db import database_setup

# from uuid import uuid4 # NOTE: used to randomize for the ids for the tables
# from models.doc import doc_response
import os
from dotenv import load_dotenv

# load in env variables
load_dotenv()

# import the env variable
FRONTEND_URL = os.getenv("FRONTEND_URL")


# function to make the tables for the database
@asynccontextmanager  # decorator for using the yield for lifespan
async def lifespan(app: FastAPI):
    # on the server start
    print("Initializing the database and making the tables")

    # set up the initial tables
    database_setup()

    # test
    # print(doc_response)

    # sets the waiting point
    yield

    # runs when the FastAPI server closes
    print("Server shutting down")


# Create the server (database set up on initial launch)
app = FastAPI(
    title="Doc Backend API", lifespan=lifespan
)  # lifespan runs before the server starts


# Middleware
# NOTE: EDIT WITH THE ENV FOR THE ROUTE SO ITS EASIER TO JK
app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL],
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
