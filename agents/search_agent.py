from config.settings import get_tavily_client
from graph.schema import AgentState
import concurrent.futures

def search_agent(state: AgentState) -> AgentState:
    """
    Search Agent (Agent 6) & Research Tree Agent (Agent 5) combined.
    Uses Tavily API to fetch search results for each sub-question concurrently.
    """
    if "ui_updates" not in state:
        state["ui_updates"] = []
        
    state["ui_updates"].append("🌐 Searching the web for resources...")
    tavily_client = get_tavily_client()
    search_data = {}
    
    # We will run these searches in parallel
    def perform_search(query):
        try:
            # We limit to top 3 per sub-question automatically
            response = tavily_client.search(query=query, search_depth="basic", max_results=3)
            return query, response.get('results', [])
        except Exception as e:
            print(f"Error during search for query '{query}': {e}")
            return query, []

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_query = {
            executor.submit(perform_search, q): q for q in state.get("sub_questions", [])
        }
        
        for future in concurrent.futures.as_completed(future_to_query):
            query, results = future.result()
            search_data[query] = results

    state["search_data"] = search_data
    return state
