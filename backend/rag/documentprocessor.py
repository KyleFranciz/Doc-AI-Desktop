# this file controls adding document data into the vector database and regular SQLite Database


# Document Processor Class (Controls the db and vector embedding processes)
from typing import Dict, List


class DocumentProcessor:
    # function to handle the process of making the new document (adding to db and vector database)
    def process_new_document(
        self,
        doc_id: str = None,
        content: List[List[str]] = None,
        metadata: List[Dict] = None,
    ):
        # embed the content with the batch processing
        # add the emedded data to the vector store
        pass

    def update_document(self, doc_id, new_content, new_metadata):
        pass

    def delete_document():
        pass

    pass
