import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from tavily import TavilyClient

# Load environment variables
load_dotenv()

# Verify required keys are present
REQUIRED_KEYS = ["GROQ_API_KEY", "TAVILY_API_KEY"]
for key in REQUIRED_KEYS:
    if not os.environ.get(key):
        raise ValueError(f"Missing required environment variable: {key}")

def get_llm(temperature=0):
    """Initializes and returns the Groq LLM."""
    return ChatGroq(model="llama-3.3-70b-versatile", temperature=temperature)

def get_tavily_client():
    """Initializes and returns the Tavily Search API client."""
    return TavilyClient(api_key=os.environ.get("TAVILY_API_KEY"))
