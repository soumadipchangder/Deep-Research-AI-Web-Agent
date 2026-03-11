# 🌍 Deep Research AI Web Search Agent

A **production-grade multi-agent research system** that retrieves live internet information and generates structured answers using **LLM reasoning**, **web search tools**, and **agent orchestration**.

Built using:

- **LangGraph** for agent workflow orchestration
- **Groq (Llama-3.3-70B)** for high-performance LLM inference
- **Tavily API** for real-time web search and information retrieval
- **Streamlit** for an interactive user interface

The system simulates a **research assistant pipeline**, where multiple specialized agents collaborate to gather, analyze, verify, and synthesize information.

This project was developed as part of the **Slooze AI Engineer Technical Challenge**.

---

# 🚀 Key Features

### 🧠 Conversational Memory
The system retains the **last five conversation turns**, enabling contextual understanding of follow-up queries.

### 🤖 Multi-Agent Architecture
The workflow is composed of **specialized micro-agents**, each responsible for a specific stage of the research process.

### 🔎 Deep Research Pipeline
Complex queries are decomposed into **3–5 sub-questions**, allowing the system to perform deeper exploration across multiple sources.

### 🔁 Self-Correcting Responses
A **critic agent** evaluates whether the generated answer aligns with retrieved sources before returning the final response.

### 📊 Confidence Scoring
Each response includes a **confidence score** derived from context quality and reasoning alignment.

### 🔗 Transparent Source Attribution
All responses include **expandable source links**, ensuring transparency and traceability.

---

# 🧠 System Architecture

The system operates as a **multi-agent workflow orchestrated with LangGraph**.


User Query
↓
Planner Agent
↓
Query Decomposition (3–5 Sub-Questions)
↓
Search Agent (Tavily API)
↓
Content Extraction Agent
↓
Reasoning Agent (LLM - Groq)
↓
Critic Agent (Verification)
↓
Confidence Agent
↓
Final Answer + Sources


Each stage acts as a **node in the LangGraph state graph**, enabling modular and scalable orchestration.

---

# 🛠 Project Structure


ai-web-search-agent/
├── app.py # Main Streamlit application
│
├── agents/ # Specialized LangGraph agents
│ ├── planner_agent.py # Query rewriting & research planning
│ ├── search_agent.py # Tavily concurrent web search
│ ├── extractor_agent.py # Structuring raw web results
│ ├── reasoning_agent.py # LLM-powered answer synthesis
│ ├── critic_agent.py # Verification and fact checking
│ └── confidence_agent.py # Confidence scoring
│
├── graph/
│ ├── workflow.py # LangGraph workflow definition
│ └── schema.py # Shared AgentState definition
│
├── config/
│ └── settings.py # Configuration and API keys
│
├── utils/
│ ├── memory.py # Conversation memory management
│ └── prompts.py # Prompt templates
│
├── requirements.txt
└── README.md


---

# ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/soumadipchangder/Deep-Research-AI-Web-Agent
cd Deep-Research-AI-Web-Agent
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 🔑 Environment Configuration

Create a .env file or configure environment variables with the following keys:

```
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

These APIs are required for:

- Groq → LLM reasoning
- Tavily → Web search and retrieval

▶️ Running the Application

Start the Streamlit application locally:

```bash
streamlit run app.py
```

Once launched, open the local URL shown in the terminal to interact with the AI research assistant.

💡 Example Usage
Example Query
What are the latest MacBook specifications released in 2026?
Example Output

Answer

Recent MacBook Pro models feature Apple's latest M5 family chips, offering improved AI acceleration, GPU performance, and energy efficiency. The new models also introduce enhanced battery life and improved display capabilities.

Sources

https://example.com/article1

https://example.com/article2

Confidence Score

0.87

🧩 Design Decisions
Agent-Based Architecture

The system distributes responsibilities across multiple agents, improving modularity and maintainability.

LangGraph Orchestration

LangGraph provides structured workflow orchestration where each research stage operates as a graph node.

Web + LLM Hybrid Reasoning

Instead of relying solely on LLM knowledge, the system retrieves live information from the internet to produce up-to-date responses.

Verification Layer

A dedicated critic agent ensures generated responses remain aligned with retrieved context.

Transparency

Providing source attribution and confidence scoring improves trust and explainability.

🔮 Future Improvements

Potential enhancements include:

- Vector database memory (ChromaDB / Pinecone)
- Autonomous multi-step research loops
- Improved ranking and filtering of search results
- Streaming responses
- Integration with academic search APIs
- Multi-LLM support
- Cloud deployment with persistent memory

👨‍💻 Author

Soumyadip Changder

GitHub
https://github.com/soumadipchangder

📄 License

This project was developed as part of the Slooze AI Engineer Technical Challenge.
