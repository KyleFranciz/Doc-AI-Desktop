# This file controls adding document data into the vector database and regular SQLite Database
# Document Processor Class (Orchastration Layter that controls the db and vector embedding processes)
from datetime import date
import datetime
from typing import Dict, List
from uuid import uuid4
from rag.embedding_model import batch_embed_documents
from rag.vector_store import ChromaDocumentVectorStore, get_collection_name
import db.db as db_utils


# Handles the Orchastration of saving and processing the documents
class DocumentProcessor:
    # core essentials
    def __init__(self, vectorStore: ChromaDocumentVectorStore) -> None:
        # gets instanciated on creation
        self.vectorStore = ChromaDocumentVectorStore()

    # function to generate metadata for additional context
    def generate_metadata(
        self, doc_id: str, source_path: str, doc_type: str, content: str, chunk_idx: int
    ) -> Dict:
        """Generates metadata for each chunk to make ready for packaging in Vector Store"""
        # build the metadata to be passed into the vectorStore
        return {
            "doc_id": doc_id,
            "source_path": source_path,
            "doc_type": doc_type,
            "content": content,
            "chunk_idx": chunk_idx,
            "chunk_length": len(content),
        }

    # function to get the data based on file type, use different parsing methods
    def choose_collection_strategy(self, doc_metadata: Dict) -> str:
        """Chooses where to send the file data to based on file type from metadata"""
        return get_collection_name(doc_metadata["doc_type"], doc_metadata["source_path"])

    # function to handle the process of making the new document (adding to db and vector database)
    def process_new_document(
        self,
        doc_id: str,
        content: List[str],
        metadata: List[Dict],
    ):
        """Ingests new document data into where it needs to go database and vector store"""
        # get the collection name
        collection_name = self.choose_collection_strategy(metadata)

        # create the chunkID per chunk
        chunk_ids = [f"{doc_id}:{idx}:{uuid4().hex}" for idx in range(len(content))]

        # make chunk metadata to pass into vectorDB
        chunk_metadata = [
            self.generate_metadata(
                doc_id=doc_id, 
                source_path=metadata["source_path"], 
                doc_type=metadata["doc_type"], 
                content=text, 
                chunk_idx=idx ) 
            for idx, text in enumerate(content)
        ]

        # break the text into 100 word chunks in a list to help with embedding properly
        embeddings = batch_embed_documents(content)
        
        # create the collection to add to the vector store in case its note made yet
        self.vectorStore.get_or_make_collection(collection_name=collection_name)
        
        # store the embeddin in the vector collection
        self.vectorStore.store_embedding_in_collection( collection_name=collection_name, document_id=chunk_ids, document_embeddings=embeddings, text=content, rich_metadata=chunk_metadata)

        # make sure I know what year and time this was stored
        now = datetime.datetime.utcnow().isoformat()

        # add embedding data into documents
        db_utils.make_exection("INSERT INTO documents (id, title, source_path, content_hash, created_at, updated_at) VALUES(?, ?, ?, ?, ?, ?)",[metadata["title"], metadata["source_path"], metadata["content_hash"], now, now])

        # add chunk data into the database
        for idx, text in enumerate(content):
            db_utils.make_exection("INSERT INTO chunks (id, document_id, chunk_index, text) VALUES (?, ?, ?, ?)", [chunk_ids[idx], doc_id, idx, text])
        
        

    def update_document(self, doc_id:str, new_content:List[str], new_metadata: Dict):
        """Updates the document if user adds new data and resubmits the same file"""
        self.delete_document(doc_id)
        self.process_new_document(doc_id, new_content, new_metadata)
        pass

    def delete_document(self, doc_id:str):
        """Deletes the document from the vector store and the database if needed"""
        # delete the document from chroma
        self.vectorStore.delete_document_completely(doc_id)
        # delete from the database
        db_utils.make_exection("DELETE FROM documents WHERE id = ?", [doc_id])

    def reprocess_with_new_model(self, doc_id:str):
        """Reprocesses the file with a different model if needed"""
        # get the chunks from the document
        rows = db_utils.make_query("SELECT chunk_index, text FROM chunks WHERE document_id = ? ORDER BY chunk_index", [doc_id])

        # get the text from the chunks
        content = [row["text"] for row in rows]

        # get the document id
        doc_row = db_utils.make_query("SELECT id, title, source_path, content_hash FROM documents WHERE id = ?", [doc_id])[0]
        

        # format the new metadata
        metadata = {
            "title": doc_row["title"],
            "source_path": doc_row["source_path"],
            "doc_type": doc_row["source_path"].split(".")[-1],
            "content_hash": doc_row["content_hash"],
        }
        
        # delete the existing documents
        self.delete_document(doc_id)
        # process the new data that we pulled before the delete
        self.process_new_document(doc_id, content, metadata)

    pass
