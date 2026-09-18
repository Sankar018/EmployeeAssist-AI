from langchain_google_genai import ChatGoogleGenerativeAI
from config import GOOGLE_API_KEY

def create_llm():
    llm = ChatGoogleGenerativeAI(
        model = "gemini-3.7-flash",
        google_api_key=GOOGLE_API_KEY
    )
    return llm
