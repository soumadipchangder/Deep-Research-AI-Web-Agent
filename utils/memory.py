import streamlit as st

def init_memory():
    """Initializes Streamlit session state for chat history if it doesn't exist."""
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
        
def add_to_history(role: str, content: str):
    """Appends a new turn to the chat history, capping at the last 5 turns."""
    st.session_state.chat_history.append({"role": role, "content": content})
    # Keep only the last 5 turns (each turn is one message, so we keep 10 messages: 5 user + 5 assist)
    # Actually, the requirement says "Store the last 5 conversation turns." A turn is a Q+A pair.
    if len(st.session_state.chat_history) > 10:
        st.session_state.chat_history = st.session_state.chat_history[-10:]

def get_formatted_history() -> str:
    """Returns the chat history as a formatted string for the LLM prompt."""
    if not st.session_state.chat_history:
        return "No previous conversation history."
        
    history_str = ""
    for msg in st.session_state.chat_history:
        role = "User" if msg["role"] == "user" else "Assistant"
        history_str += f"{role}: {msg['content']}\n"
    return history_str.strip()
