# 🤖 AI Agent Chatbot with LangGraph, LangChain, and Groq

An intelligent, modular AI chatbot powered by **Groq’s LLaMA-3**, **LangChain Agents**, and **LangGraph** — designed to simulate human-like reasoning, integrate live web search, and adapt its behavior through custom prompts.

> 🔍 **Goal**: To build a production-ready AI system that can **reason**, **search**, and **respond** dynamically—mimicking how a human expert might solve a query with both memory and internet access.

---

## 🎯 What Are We Achieving?

✅ Creating an **LLM-powered agent** that does more than just chat—it **thinks**, **uses tools**, and **adjusts behavior** based on user-defined prompts.

✅ Giving users the power to define **agent personality**, switch between powerful **Groq-hosted models**, and even turn **web search on/off** as needed.

✅ Building a **full-stack framework** that bridges LLM reasoning, API integration, and interactive UI—perfect for **real-world applications** like:
- AI tutors or teaching assistants
- Research companions with web search
- Customer service bots with tool integration
- RAG assistants with modular control

---

## 🌐 Live Components

| Component   | Purpose                                       |
|-------------|-----------------------------------------------|
| `ai_agent.py` | Core LangGraph + LangChain agent logic       |
| `backend.py`  | FastAPI backend to serve agent as a web API  |
| `frontend.py` | Streamlit frontend for end-user interaction  |

---

## 🧠 Features

- 🧩 **ReAct-based AI Agent** using LangGraph's dynamic planning
- 🔄 Switchable LLMs (`llama-3.3-70b-versatile`, `mixtral-8x7b`)
- 🌍 **Web search tool** (Tavily) for real-time information access
- ✏️ Define your agent's **personality** via system prompt
- 🔗 Plug-and-play architecture: Easy to extend or integrate

---

## ⚙️ Tech Stack

- **LLMs**: Groq-hosted LLaMA-3, Mixtral
- **Agent Framework**: LangGraph, LangChain
- **Tools**: Tavily Web Search
- **Backend**: FastAPI
- **Frontend**: Streamlit
- **Environment Management**: dotenv (.env file)

---

{
  "model_name": "llama-3.3-70b-versatile",
  "model_provider": "Groq",
  "system_prompt": "Act as an AI tutor who helps students solve problems",
  "messages": ["What is the difference between BERT and LLaMA?"],
  "allow_search": true
}

