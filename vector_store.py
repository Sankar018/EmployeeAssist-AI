from langchain_community.vectorstores import Chroma
from config import GOOGLE_API_KEY
from pdf_loader import load_documents
from text_splitter import split_documents
from embedding import create_embedding

CHROMA_DIR = "chroma_db"

def create_vector_store():

    documents = load_documents()
    chunks = split_documents(documents)
    embeddings = create_embedding()

    # Create ChromaDB and store embeddings
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DIR
    )

    return vector_store
