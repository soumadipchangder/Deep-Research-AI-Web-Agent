from langchain_core.prompts import PromptTemplate

# Follow-up Detection
FOLLOWUP_PROMPT = PromptTemplate(
    input_variables=["chat_history", "query"],
    template="""You are a user query analyzer. Determine whether the current question requires previous conversation context, or if it is a completely new query.

Conversation history:
{chat_history}

Current Question: {query}

Return ONLY:
FOLLOW_UP
or
NEW_QUERY
"""
)

# Query Rewriting
REWRITE_PROMPT = PromptTemplate(
    input_variables=["chat_history", "query"],
    template="""You are a query rewriting assistant. The user has asked a follow-up question. 
Rewrite the user's latest query into a standalone query that contains all necessary context from the conversation history.

Conversation history:
{chat_history}

Follow-up query: {query}

Rewritten standalone query (return ONLY the rewritten query):
"""
)

# Research Planner
PLANNER_PROMPT = PromptTemplate(
    input_variables=["query"],
    template="""You are a Research Planner. Break this research question down into 3-5 smaller, highly specific sub-questions that need to be searched to provide a comprehensive answer.

Question: {query}

Return ONLY the sub-questions separated by newlines, with no bullet points or numbering.
"""
)

# Reasoning & Synthesis
REASONING_PROMPT = PromptTemplate(
    input_variables=["context", "query"],
    template="""You are an expert AI Research Assistant. Answer the user's query comprehensively using ONLY the provided research notes. 

Research Notes:
{context}

Query: {query}

Instructions:
1. Synthesize the information clearly.
2. If multiple sources agree, state it. If they conflict, mention the differing views.
3. Be professional and objective.
4. IMPORTANT: Include citations to the sources in your answer if it makes sense (e.g. "According to Source X..." or [Source Title]).

Your Answer:
"""
)

# Critic/Verification
CRITIC_PROMPT = PromptTemplate(
    input_variables=["context", "answer"],
    template="""You are an AI fact-checker. 
Check whether the provided answer is fully supported by the research notes.

Research Notes:
{context}

Draft Answer:
{answer}

Return ONLY:
VALID
or
NEEDS_REVISION
"""
)
