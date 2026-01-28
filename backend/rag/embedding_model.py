"""This file will be used to convert text from text, pdf and other files into embedding to pass into chroma"""

# imports
from typing import List
from langchain_ollama import OllamaEmbeddings


# embedding model
embedder = OllamaEmbeddings(model="nomic-embed-text-v2-moe:latest", temperature=0.1)


# function to handle embedding a list of text
def embed_document(texts: List[str]) -> List[List[float]]:
    """Returns a list of vectors"""
    document_embedding = embedder.embed_documents(texts=texts)
    return document_embedding


# function to batch the document into seperate chunks to make it easier for the document to be used
def batch_embed_documents(texts: List[str], batch_size: int = 100):
    # create a dictionary to return the all the batches
    all_batches = []

    # get each word starting from the first word for the word length and skip every 100 words
    for idx in range(0, len(texts), batch_size):
        # idx jumps every 100 and adds that value to the batch size keeps the range between those numbers
        batch = texts[idx : idx + batch_size]
        # embed the batch, embed each word to pass so its ready to send to chroma
        batch_embedding = embed_document(batch)
        # add the embedding to array of batches to return
        all_batches.extend(batch_embedding)

    # return all batches
    return all_batches


# function to handle question from the user
def embed_query(text: str) -> List[float]:
    """This returns a single list of vectors"""
    question_embedding = embedder.embed_query(text=text)
    return question_embedding


# function to get the embedding dimmentions
def get_embedding_dimmensions(vectors: List[List[float]]) -> int:
    """This function returns the length of the vectors so that we can ge the sizing"""
    return len(vectors)
