from langchain_core.output_parsers import StrOutputParser
from search import create_retriever
from model import create_llm
from prompt import create_prompt

def format_documents(documents):
    return "\n\n".join( 
        document.page_content 
        for document in documents 
    )

def create_rag_chain():
    # Create retriever 
    retriever = create_retriever(k=3)
    # Create Gemini LLM 
    llm = create_llm()
    # Create prompt
    prompt = create_prompt()

    # Build RAG chain
    rag_chain = (
        {
            "context": lambda x: format_documents(
                retriever.invoke(x["question"])
            ),
            "question": lambda x: x["question"],
            "chat_history": lambda x: x["chat_history"]
        }
        | prompt
        | llm
        | StrOutputParser()
    )
    return rag_chain

if __name__ == "__main__":
    rag_chain = create_rag_chain()
    question = str(input("Ask question: "))
    answer = rag_chain.invoke(question)
    print("\n================================") 
    print("RAG ANSWER") 
    print("================================") 
    print(f"\nQuestion: {question}") 
    print("\nAnswer:") 
    print(answer)