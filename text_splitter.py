from langchain_text_splitters import RecursiveCharacterTextSplitter
from pdf_loader import load_documents

def split_documents(documents):
    text_spliter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200
    )

    chunks = text_spliter.split_documents(documents)

    return chunks
