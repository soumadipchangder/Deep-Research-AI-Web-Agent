from graph.schema import AgentState

def confidence_agent(state: AgentState) -> AgentState:
    """
    Confidence Estimator Agent (Agent 10).
    Produces a heuristic score based on the context parsing and verification loops.
    """
    # Simple heuristic scoring based on:
    # 1. Number of unique sources (caps at 5 for scoring)
    # 2. Revisions needed (more revisions = slightly less confidence, despite eventual fix)
    # 3. Size of context available
    
    context = state.get("research_context", "")
    sources = state.get("sources", [])
    revisions = state.get("revision_count", 0)
    
    # Base confidence
    score = 0.5
    
    # Factor 1: Citations
    num_sources = len(sources)
    source_boost = min(num_sources * 0.1, 0.4) # up to +0.4 for multiple sources
    
    # Factor 2: Context Richness Context
    context_words = len(context.split())
    if context_words > 500:
        context_boost = 0.15
    elif context_words > 100:
        context_boost = 0.05
    else:
        # Penalize severely if no or little context found
        context_boost = -0.3
        
    # Factor 3: Revisions
    # If the system struggled to verify, maybe facts were hard to align
    revision_penalty = revisions * 0.05
    
    total_score = min(max(score + source_boost + context_boost - revision_penalty, 0.0), 1.0)
    
    state["confidence_score"] = round(total_score, 2)
    state["ui_updates"].append(f"✅ Final answer generated (Confidence: {state['confidence_score']})")
    
    return state
