import streamlit as st
from config.settings import load_dotenv # ensures we crash early if missing env
from graph.workflow import create_workflow
from utils.memory import init_memory, add_to_history

# Initialize page config
st.set_page_config(
    page_title="Deep Research AI",
    page_icon="🌍",
    layout="wide"
)

# Render UI Title
st.title("🌍 Deep Research AI Web Agent")
st.markdown("A multi-agent conversational system powered by LangGraph, Groq, and Tavily.")

# Initialize Session Memory
init_memory()

# Initialize graph exactly once
@st.cache_resource
def get_graph():
    return create_workflow()

graph = get_graph()

# Display Chat History
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg.get("sources"):
            with st.expander("Sources Used"):
                for source in msg["sources"]:
                    st.write(f"- {source}")
        if msg.get("confidence") is not None:
            st.metric("Confidence Score", msg["confidence"])

# Chat Input Area
user_query = st.chat_input("Ask a complex research question...")

if user_query:
    # Immediately render the user's message
    with st.chat_message("user"):
        st.markdown(user_query)
        
    # Append to memory
    add_to_history("user", user_query)
    
    # Run the graph
    with st.chat_message("assistant"):
        ui_container = st.container()
        
        with st.status("Running Deep Research...", expanded=True) as status:
            # We execute the graph node by node so we can pull state to show UI updates
            
            # Initial State
            state = {
                "original_query": user_query,
                "ui_updates": []
            }
            
            # LangGraph stream gives us the output of each node
            for output in graph.stream(state):
                for node_name, node_state in output.items():
                    # Check if there are new UI updates
                    if "ui_updates" in node_state:
                        # Print only the newest update
                        latest_update = node_state["ui_updates"][-1]
                        st.write(latest_update)
            
            status.update(label="Research Complete!", state="complete", expanded=False)
            
            # Extract final state fields
            final_node = list(output.values())[0] # The very last state dictionary
            final_answer = final_node.get("final_answer", "I couldn't find an answer.")
            sources = final_node.get("sources", [])
            confidence = final_node.get("confidence_score", 0.0)
            
        # Display Final Answer to User
        st.markdown(final_answer)
        
        # Display Sources Expanders
        if sources:
            with st.expander("Sources Used"):
                for url in sources:
                    st.write(f"- {url}")
                    
        # Display Confidence    
        if confidence:
            st.metric("Confidence Score", confidence)
            
    # Add assistant response back to memory
    # We store the extra metadata so it rerenders properly on reload
    st.session_state.chat_history.append({
        "role": "assistant",
        "content": final_answer,
        "sources": sources,
        "confidence": confidence
    })
    
    # Cap memory length (we did this in user turn but just to be safe)
    if len(st.session_state.chat_history) > 10:
        st.session_state.chat_history = st.session_state.chat_history[-10:]
