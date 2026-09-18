from pathlib import Path
from langchain_community.document_loaders import PyMuPDFLoader

DOCUMENT_DIR = Path("documents")

def load_documents():
    all_documents = []
    pdf_files = sorted(DOCUMENT_DIR.glob("*pdf"))

    for pdf_file in pdf_files:
        print(f"Loading: {pdf_file.name}")
        loader = PyMuPDFLoader(str(pdf_file))
        documents = loader.load()

        all_documents.extend(documents)

    return all_documents
