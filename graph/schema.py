from typing import TypedDict, List, Dict, Any

class AgentState(TypedDict):
    """
    Represents the shared memory state of the LangGraph Multi-Agent system.
    """
    
    # Original user input
    original_query: str
    
    # Processed query (either original or rewritten with context)
    query: str
    
    # Flag to determine routing
    is_follow_up: bool
    
    # Results from Planner Agent
    sub_questions: List[str]
    
    # Results from Search Agent (tree)
    # Mapping of {sub_question: [list of search results]}
    search_data: Dict[str, List[Dict[str, str]]]
    
    # Formatted context from Extractor Agent
    research_context: str
    
    # First draft of the answer from Reasoning Agent
    draft_answer: str
    
    # Critic agent review ('VALID' or 'NEEDS_REVISION')
    critic_status: str
    
    # Counter to limit the number of revision loops
    revision_count: int
    
    # The final, verified answer shown to the user
    final_answer: str
    
    # Confidence score given by Confidence Estimator (0.0 to 1.0)
    confidence_score: float
    
    # List of unique URLs used to answer the query
    sources: List[str]
    
    # UI updates list for st.status tracking
    ui_updates: List[str]
