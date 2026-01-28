# This is the main agent of the app

# imports
from langchain_ollama import ChatOllama
from langchain.messages import SystemMessage, HumanMessage

# create doc agent
doc_main = ChatOllama(model="qwen3:8b", temperature=0)

# create the system message
system_message = SystemMessage(
    """
    You are a friendly document summary agent, you are tasked with giving the user information related
    to the document/documents assigned as well as answering only questions pertainaing to the document to the
    best of your abilities. If the question from the user does not have anything to do with the document/documents
    assigned tell the user that you are not able to answer the question unless it has to do with the information from 
    the document/documents.
    """,
)


# function to get the users input and generate a response
def get_answer_from_doc(question: str, document_info: str):
    # might bring in the data from the vector database to help add context

    # get the users question
    user_message = HumanMessage(question)

    messages = [system_message, user_message]
    # return the answer to from doc
    return doc_main.invoke(messages)
