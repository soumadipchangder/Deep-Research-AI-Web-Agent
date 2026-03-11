# 🌍 Deep Research AI Web Search Agent

A production-grade, multi-agent conversational system using **LangGraph**, **Groq (Llama-3.3-70b)**, and the **Tavily API**. Built with a rich **Streamlit** user interface suitable for deployment on Hugging Face Spaces.

## 🚀 Features
- **Conversational Memory**: Retains the last 5 turns of conversation to understand follow-up queries contextually.
- **Micro-Agent Architecture**: Discrete agents handle planning, web searching, content extraction, reasoning, source-criticism, and confidence estimation.
- **Deep Research Pipeline**: Breaks down complex queries into 3-5 sub-questions and concurrently searches the web to build a robust context tree.
- **Self-Correcting**: Features a self-critic loop to ensure the draft answer aligns properly with the source material before showing it to the user.
- **Transparent Output**: Real-time progress tracing, confidence scoring, and expanding URL source lists display clearly in the UI.

## 🛠 Project Structure
```text
ai-web-search-agent/
├── app.py                      # Main Streamlit App
├── agents/                     # Specialized LangGraph nodes
│   ├── planner_agent.py        # Follow-ups, rewriting & tree generation
│   ├── search_agent.py         # Tavily concurrent sub-query search
│   ├── extractor_agent.py      # Structuring raw web results
│   ├── reasoning_agent.py      # Groq-powered drafted answer synthesis
│   ├── critic_agent.py         # Verification and fact-checking
│   └── confidence_agent.py     # Heuristic scoring based on context
├── graph/                      # LangGraph definition
│   ├── workflow.py             # Node / Edge assembly (StateGraph)
│   └── schema.py               # Shared AgentState typed dict
├── config/                     # Configuration and keys
│   └── settings.py             
├── utils/                      # Helper tools
│   ├── memory.py               # Streamlit session state wrappers
│   └── prompts.py              # Centralized prompt templates
├── requirements.txt            
└── README.md
```

## ⚙️ Installation & Usage

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Environment Variables**:
   Set the following variables in a `.env` file or in your Hugging Face Space Secrets:
   - `GROQ_API_KEY`: Your Groq API key
   - `TAVILY_API_KEY`: Your Tavily Search API key

3. **Run locally**:
   ```bash
   streamlit run app.py
   ```
