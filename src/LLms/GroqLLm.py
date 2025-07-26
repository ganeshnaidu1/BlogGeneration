from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

class GroqLLm:
    def __init__(self):
        load_dotenv()
    
    def get_llm(self):
        try:
            groq_api_key = os.getenv("GROQ_API_KEY")
            if not groq_api_key:
                print("Error: GROQ_API_KEY not found in environment variables")
                return None
            
            os.environ["GROQ_API_KEY"] = groq_api_key
            self.llm = ChatGroq(
                model_name="llama3-8b-8192",
            )
            return self.llm
        except Exception as e:
            print(f"Error initializing GroqLLm: {e}")
            return None