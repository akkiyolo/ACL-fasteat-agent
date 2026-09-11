from tavily import TavilyClient
from dotenv import load_dotenv
from langchain.tools import tool
from typing import Dict, Any
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

load_dotenv()

tavilyclient = TavilyClient()

@tool
def web_search(query: str) -> Dict[str, Any]:
    """Search the web for the given query using Tavily and return the results."""
    logging.info(f"searching for {query}")
    return tavilyclient.search(query)