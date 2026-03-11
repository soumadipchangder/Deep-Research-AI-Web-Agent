from config.settings import get_llm
from utils.prompts import FOLLOWUP_PROMPT, REWRITE_PROMPT, PLANNER_PROMPT
from utils.memory import get_formatted_history
from graph.schema import AgentState
import streamlit as st

def planner_agent(state: AgentState) -> AgentState:
    """
    Acts as the Conversation Memory, Follow-up Detection, Query Rewriting, and Research Planner Agents.
    Executes sequentially via Groq calls.
    """
    llm = get_llm(temperature=0)
    chat_history = get_formatted_history()
    user_query = state.get("original_query", "")
    
    state["ui_updates"] = state.get("ui_updates", [])
    state["ui_updates"].append("🤔 Thinking about query context...")
    
    # 1. Follow-up Detection (Agent 2)
    follow_chain = FOLLOWUP_PROMPT | llm
    follow_res = follow_chain.invoke({
        "chat_history": chat_history,
        "query": user_query
    }).content.strip().upper()
    
    is_follow_up = "FOLLOW_UP" in follow_res
    state["is_follow_up"] = is_follow_up
    
    # 2. Query Rewriting (Agent 3) - Only if it's a follow-up
    if is_follow_up and len(st.session_state.chat_history) > 0:
        state["ui_updates"].append("📝 Rewriting query based on conversation history...")
        rewrite_chain = REWRITE_PROMPT | llm
        rewritten_query = rewrite_chain.invoke({
            "chat_history": chat_history,
            "query": user_query
        }).content.strip()
        state["query"] = rewritten_query
    else:
        state["query"] = user_query
        
    # 3. Research Planner (Agent 4)
    state["ui_updates"].append("🔎 Planning research questions...")
    planner_chain = PLANNER_PROMPT | llm
    raw_sub_questions = planner_chain.invoke({
        "query": state["query"]
    }).content.strip()
    
    # Parse sub-questions
    sub_questions = [
        q.strip().lstrip("-").lstrip("1234567890. ") 
        for q in raw_sub_questions.split("\n") 
        if q.strip()
    ][:5] # limit to 5
    
    state["sub_questions"] = sub_questions
    return state
