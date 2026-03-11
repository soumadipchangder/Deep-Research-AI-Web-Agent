from config.settings import get_llm
from utils.prompts import REASONING_PROMPT
from graph.schema import AgentState

def reasoning_agent(state: AgentState) -> AgentState:
    """
    Reasoning Agent (Agent 8).
    Synthesizes the extracted research context to form a drafted response.
    """
    if "ui_updates" not in state:
        state["ui_updates"] = []

    state["ui_updates"].append("🧠 Reasoning over sources to generate draft...")
    llm = get_llm(temperature=0.2)
    
    chain = REASONING_PROMPT | llm
    
    draft = chain.invoke({
        "context": state.get("research_context", ""),
        "query": state.get("query", "")
    }).content.strip()

    state["draft_answer"] = draft
    return state
