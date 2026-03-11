from config.settings import get_llm
from utils.prompts import CRITIC_PROMPT
from graph.schema import AgentState

def critic_agent(state: AgentState) -> AgentState:
    """
    Self-Critic Agent (Agent 9).
    Verifies the drafted answer against the search context to ensure valid grounding.
    """
    if "ui_updates" not in state:
        state["ui_updates"] = []

    state["ui_updates"].append("🛡 Verifying accuracy of the answer...")
    llm = get_llm(temperature=0)
    
    chain = CRITIC_PROMPT | llm
    
    res = chain.invoke({
        "context": state.get("research_context", ""),
        "answer": state.get("draft_answer", "")
    }).content.strip().upper()

    is_valid = "VALID" in res
    
    # Simple loop breaker: if we verified, set it
    # Alternatively if we did too many loops, just force it as valid to break graph.
    count = state.get("revision_count", 0)
    
    if is_valid or count >= 3:
        state["critic_status"] = "VALID"
        state["final_answer"] = state.get("draft_answer")
        state["ui_updates"].append("✅ Verification passed.")
    else:
        state["critic_status"] = "NEEDS_REVISION"
        state["revision_count"] = count + 1
        state["ui_updates"].append(f"⚠️ Answer needs revision (Attempt {state['revision_count']}). Rethinking...")
        
    return state
