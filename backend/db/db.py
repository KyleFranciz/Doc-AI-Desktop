# handles creation of the database
import os
from dotenv import load_dotenv
import sqlite3

# might add in a logger

# bring in the env variables to use
load_dotenv()

# store the variables to use in this file
DB_PATH = os.getenv("DB_PATH")


# helper function that establishes a connection and helps with queries
def use_database():
    # create connection
    connection = sqlite3.connect(DB_PATH)
    # create access to the rows to make accessing queries easier
    connection.row_factory = sqlite3.Row
    try:
        # yeild the data
        yield connection
    finally:
        # close the connection
        connection.close()


# function to create the basic structure of the db
def database_setup():
    # handles the closing of the db after the action is done
    with sqlite3.connect(DB_PATH) as connection:
        # create the cursor that will do the actions needed
        cursor = connection.cursor()  # connects to the database file

        # create the tables that are needed one by one

        # chats table
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS chat_sessions (id TEXT PRIMARY KEY, title TEXT NOT NULL, created_at TEXT NOT NULL)"
        )

        # chat_messages table (delete all chat messages id the session is deleted)
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS chat_messages (id TEXT PRIMARY KEY, session_id TEXT NOT NULL, role TEXT NOT NULL, message TEXT NOT NULL ,FOREIGN KEY (session_id) REFERENCES chat_sessions (id) ON DELETE CASCADE)"
        )

        # documents table
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS documents (id TEXT PRIMARY KEY, title TEXT NOT NULL, source_path TEXT, content_hash TEXT NOT NULL, created_at TEXT NOT NULL, updated_at TEXT NOT NULL)"
        )

        # chunks table (delete all the chunks if the document is deleted)
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS chunks (id TEXT PRIMARY KEY, document_id TEXT NOT NULL, chunk_index INTEGER NOT NULL, text TEXT NOT NULL, FOREIGN KEY (document_id) REFERENCES documents(id) ON DELETE CASCADE)"
        )

        # make the changes to the database
        connection.commit()


# funtion to make addition to the database
def make_exection(query, parameters):
    pass


def make_query(query, parameters):
    pass
