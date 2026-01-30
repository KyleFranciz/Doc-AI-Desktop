"""This file is to make a chromaDB class to be able to store the data that needs to be passed in"""

# imports
# NOTE: PersistentClient is for me to be able to keep the vector data running on the application when its running
from typing import Dict, List
from chromadb import Collection, chromadb
from chromadb.api.client import Client
from platformdirs import user_data_dir
from dotenv import load_dotenv
import os

# from pathlib import Path # use to help with finding the source path

# NOTE: MIGHT CREATE COLLECTIONS PER PROJECT IF I ADD IN A PROJECT FEATURE FOR PERSISTENCE PER PROJECTS

# load env variable
load_dotenv()

APP_NAME = os.getenv("APP_NAME")
APP_AUTHOR = os.getenv("APP_AUTHOR")

# data directory for prod as well as dev
data_path = user_data_dir(appname=APP_NAME, appauthor=APP_AUTHOR)
chroma_path_for_storage = f"{data_path}/chroma_data"

# defaults
default_collection_name = "doc_context_collection"


# Chroma Class
class ChromaDocumentVectorStore:
    # this function creates the chromadb client in the disk
    def __init__(self, path: str = chroma_path_for_storage) -> None:
        self.client: Client = chromadb.PersistentClient(path=path)
        self.collection: Collection = None

    # this handles the creation or getting data from chroma collection in the db
    def get_or_make_collection(
        # only using one big collection to store every thing for global connection
        self,
        collection_name: str = default_collection_name,
    ):  # defaults to this
        # creates or gets collection if exists, useful for app start
        self.collection = self.client.get_or_create_collection(collection_name)

    def get_collection_name(self, doc_type: str, source: str):
        # file type
        file_types = {".pdf, .txt, .md"}
        # seperate an text and get the file type
        type_of_doc = doc_type.lower().split()

        # check to see if the file type is doc_type
        if {} in type_of_doc:
            pass
        # filter the data by metadata

        pass

    # function to store data in chroma
    def store_embedding_in_collection(
        self,
        collection_name: str = default_collection_name,  # name for the collection
        document_id: str = None,  # ids for the documents
        document_embeddings: List[
            List[float]
        ] = None,  # all the embeddings from I created from the chunks from the document
        text: List[str] = None,  # text that coralates with the vectors
        rich_metadata: List[
            Dict
        ] = None,  # meta data to help with storing additional data
    ):
        # check if there is a collection already
        if self.collection is None:
            self.collection = ChromaDocumentVectorStore.get_or_make_collection(
                collection_name
            )

        # add the items to the collection
        # NOTE: Remove print results after I test that it works
        results = self.collection.add(
            ids=document_id,  # adding in randomly generated ids using uuid
            embeddings=document_embeddings,  # emeddings from the embedder that embedded the doc
            documents=text,  # text info for cross reference to be able to show a result
            metadatas=rich_metadata,  # help with the filtering
        )
        # print the result (might not be able to)
        print(results)

    # function to search for similar result for the question in the database
    def search_for_in_store(
        self,
        collection_name: str = default_collection_name,  # name for the collection
        query_embedding: List[float] = None,  # question that was embedded
        n_results: int = 10,  # returns this amount of results
    ):
        pass

    # function to search across all the collections if needed
    def search_across_all_collections(
        self, query_embedding: List[float] = None, collections: List[str] = None
    ):
        """
        query_embedding is the question that was embedded from the user

        collections are all the different collections that I want to search for the answer in
        """
        pass

    # function to delete the document data
    def delete_document_completely(self, document_id: str):
        self.collection.delete(ids=document_id)

    # function to replace the embeddings in the document
    def replace_document_embedding(
        self,
        document_id: str,  # document id that houses all info for one document
        new_embeddings: List[
            List[float]
        ],  # new embeddings to replace for the document to update the info
        new_metatadata: List[Dict],  # new metadata for filtering
    ):
        pass
