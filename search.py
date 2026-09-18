from langchain_community.vectorstores import Chroma

from embedding import create_embedding


CHROMA_DIR = "chroma_db"


def create_retriever(k=3):
    """
    Load the existing ChromaDB and create a retriever.

    k = number of relevant document chunks to retrieve.
    """

    embeddings = create_embedding()

    vector_store = Chroma(
        persist_directory=CHROMA_DIR,
        embedding_function=embeddings
    )

    retriever = vector_store.as_retriever(
        search_kwargs={"k": k}
    )

    return retriever
