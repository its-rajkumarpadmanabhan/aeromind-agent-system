<img width="1908" height="992" alt="image" src="https://github.com/user-attachments/assets/b03c5324-ff92-4202-8727-b7b83ec407f0" />
---

# 🧠 AeroMind: Enterprise Market Intelligence System

AeroMind is an autonomous multi-agent corporate research and intelligence orchestration network. Instead of a human manually spending hours compiling data, this system utilizes an interconnected squad of AI specialized agents that collaborate asynchronously to generate boardroom-ready market intelligence reports in seconds.

🎯 **Live Demo:** [View Live App](https://aeromind-agent-system-qvvbh8xe6zd9zuo9sapvii.streamlit.app/)

---

## 🚀 Key Features

*   🕸️ **State-Driven Multi-Agent Workflows:** Orchestrated using **LangGraph** to manage a robust cyclic state machine with strict context preservation.
*   🕵️‍♂️ **Real-Time Web Intelligence:** Bypasses standard static LLM knowledge limits by dynamically scraping current information via a native DuckDuckGo search integration.
*   ⚡ **Ultra-Low Latency Inference:** Powered by **Groq** using hardware-accelerated **Llama 3** models for near-instant execution loops.
*   📊 **Automated Quantitative & SWOT Analysis:** Deep-dives into competitor moves, market shares, and potential risk matrices.
*   📝 **Executive Report Compilation:** Auto-compiles data streams into polished Markdown reports complete with a one-click asset download mechanism.

---
💻 Tech Stack
Core Logic: Python 3.11+

Agent Orchestration: LangGraph (LangChain ecosystem)

LLM Inference Server: Groq Cloud API

Models Utilized: Llama-3-8b-Instant / Llama-3-70b-Versatile

User Interface: Streamlit Framework

Hosting: Streamlit Community Cloud (Snowflake CI/CD pipeline)

---
## 🛠️ System Architecture & Workflow

The network passes data across a centralized memory graph state (`AgentState`) through three dedicated intelligence nodes:

```text
[User Objective] 
       │
       ▼
┌──────────────┐
│  🕵️‍♂️ Researcher │ ──> Dynamic Live Web Search Engine (DDG)
└──────────────┘
       │
       ▼
┌──────────────┐
│  📊 Analyst   │ ──> Evaluates Market Trends & SWOT Matrices
└──────────────┘
       │
       ▼
┌──────────────┐
│  📝 Writer    │ ──> Compiles Executive Summary & Generates Assets
└──────────────┘
       │
       ▼
[Downloadable Executive Dossier (.md)]




