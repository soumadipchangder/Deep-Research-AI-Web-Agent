from graph.schema import AgentState

def extractor_agent(state: AgentState) -> AgentState:
    """
    Content Extraction Agent (Agent 7).
    Formats the raw search results array into a structured research context string
    that an LLM can easily consume, while building a list of unique sources.
    """
    if "ui_updates" not in state:
        state["ui_updates"] = []

    state["ui_updates"].append("📄 Extracting and structuring information...")
    
    search_data = state.get("search_data", {})
    context_lines = []
    sources_set = set()
    
    for sub_q, results in search_data.items():
        if results:
            context_lines.append(f"### Sub-Topic: {sub_q}")
            for res in results:
                title = res.get("title", "No Title")
                content = res.get("content", "No Content provided")
                url = res.get("url")
                
                context_lines.append(f"Source Title: {title}")
                if url:
                    context_lines.append(f"URL: {url}")
                    sources_set.add(url)
                
                context_lines.append(f"Snippet/Content: {content}\n")
    
    formatted_context = "\n".join(context_lines)
    
    # If no results came back across all searches, ensure we have a fallback
    if not formatted_context.strip():
        formatted_context = "No relevant information could be found from the web searches."
        
    state["research_context"] = formatted_context
    state["sources"] = list(sources_set)
    
    return state
