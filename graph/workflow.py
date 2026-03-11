from langgraph.graph import StateGraph, START, END
from graph.schema import AgentState

# Import node functions
from agents.planner_agent import planner_agent
from agents.search_agent import search_agent
from agents.extractor_agent import extractor_agent
from agents.reasoning_agent import reasoning_agent
from agents.critic_agent import critic_agent
from agents.confidence_agent import confidence_agent

def create_workflow() -> StateGraph:
    """
    Assembles the Deep Research Conversational Graph.
    """
    workflow = StateGraph(AgentState)
    
    # Add nodes
    workflow.add_node("planner", planner_agent)
    workflow.add_node("search", search_agent)
    workflow.add_node("extractor", extractor_agent)
    workflow.add_node("reason", reasoning_agent)
    workflow.add_node("critic", critic_agent)
    workflow.add_node("confidence", confidence_agent)
    
    # Add linear edges and conditionals
    workflow.add_edge(START, "planner")
    workflow.add_edge("planner", "search")
    workflow.add_edge("search", "extractor")
    workflow.add_edge("extractor", "reason")
    workflow.add_edge("reason", "critic")
    
    # Conditional edge looping backwards for synthesis if revision needed
    def route_critic(state: AgentState):
        if state.get("critic_status") == "VALID":
            return "confidence"
        return "reason" # loop back to reasoning with updated counts

    workflow.add_conditional_edges(
        "critic",
        route_critic,
        {
            "confidence": "confidence",
            "reason": "reason"
        }
    )
    
    workflow.add_edge("confidence", END)
    
    return workflow.compile()
