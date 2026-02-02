# This file controls adding document data into the vector database and regular SQLite Database
# Document Processor Class (Orchastration Layter that controls the db and vector embedding processes)
from typing import Dict, List

from rag.vector_store import ChromaDocumentVectorStore


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
        pass

    # function to get the data based on file type, use different parsing methods
    def choose_collection_strategy(self, doc_metadata: Dict) -> str:
        """Chooses where to send the file data to based on file type from metadata"""
        pass

    # function to handle the process of making the new document (adding to db and vector database)
    def process_new_document(
        self,
        doc_id: str = None,
        content: List[List[str]] = None,
        metadata: List[Dict] = None,
    ):
        """Ingests new document data into where it database and vector store"""
        # embed the content with the batch processing
        # add the emedded data to the vector store
        pass

    def update_document(self, doc_id, new_content, new_metadata):
        """Updates the document if user adds new data and resubmits the same file"""
        pass

    def delete_document(self, doc_id):
        """Deletes the document from the vector store and the database if needed"""
        pass

    def reprocess_with_new_model(self, doc_id):
        """Reprocesses the file with a different model if needed"""
        pass

    pass
