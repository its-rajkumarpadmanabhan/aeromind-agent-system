import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from langgraph.graph import StateGraph, END
from state import AgentState

# Load environment variables from your .env file
load_dotenv()

# Initialize the core models and tools
# We use temperature=0 for corporate intelligence to reduce hallucinations
llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0) 
from ddgs import DDGS

def custom_web_search(query: str) -> str:
    """A resilient search tool optimized for fresh, real-time market news."""
    try:
        with DDGS() as ddgs:
            # We add a timeline constraint or append "news 2026" mentally to ensure 
            # we are getting current architectures (Blackwell, Rubin, H200) instead of old V100s.
            optimized_query = f"{query} recent news updates 2026"
            
            results = [r for r in ddgs.text(optimized_query, max_results=4)]
            if not results:
                return "No recent search results found."
            
            formatted_results = []
            for item in results:
                formatted_results.append(f"Title: {item['title']}\nURL: {item['href']}\nSnippet: {item['body']}\n---")
            return "\n".join(formatted_results)
    except Exception as e:
        return f"Search temporarily unavailable. Proceeding with base knowledge. Error: {str(e)}"
# 1. Initialize our graph with the state schema
workflow = StateGraph(AgentState)

# ==========================================
# PRODUCTION NODE IMPLEMENTATIONS
# ==========================================

def researcher_node(state: AgentState):
    print("\n--- ACTIVATE: RESEARCHER AGENT ---")
    objective = state["task_objective"]
    
    # Using our custom native tool instead of the broken langchain wrapper
    print(f"Searching the web for: '{objective}'...")
    search_results = custom_web_search(objective)
    
    prompt = f"""You are an Expert Market Research Agent. 
    Analyze the raw web data below regarding: '{objective}'
    Extract key trends, competitor statistics, and relevant data points.
    
    Raw Search Data:
    {search_results}
    """
    
    ai_message = llm.invoke(prompt)
    print("Researcher finished compiling findings.")
    return {"messages": [ai_message]}


def analyst_node(state: AgentState):
    print("\n--- ACTIVATE: ANALYTICS AGENT ---")
    
    # Extract the previous intelligence gathered by the researcher
    latest_research = state["messages"][-1].content
    
    prompt = f"""You are a Senior Financial & Market Analyst. 
    Review this recent research report:
    {latest_research}
    
    Synthesize these findings into quantitative projections or core strategic insights. 
    Identify opportunities, threats, or numerical trends. Be concise.
    """
    
    ai_message = llm.invoke(prompt)
    print("Analyst finished compiling data projections.")
    return {"messages": [ai_message]}


def writer_node(state: AgentState):
    print("\n--- ACTIVATE: EXECUTIVE WRITER AGENT ---")
    
    # Consolidate everything that has happened in the history
    full_history = "\n\n".join([f"[{msg.type}]: {msg.content}" for msg in state["messages"]])
    
    prompt = f"""You are an Executive Communications Specialist. 
    Review the full operational log and analysis:
    {full_history}
    
    Compile a formal, high-impact Executive Intelligence Report in beautiful Markdown format. 
    Include clear headers, bullet points, and strategic recommendations.
    """
    
    ai_message = llm.invoke(prompt)
    print("Writer finished the final brief.")
    return {"messages": [ai_message], "next_node": "FINISH"}


# ==========================================
# GRAPH ORCHESTRATION CONFIGURATION
# ==========================================

# Add the live physical nodes
workflow.add_node("researcher", researcher_node)
workflow.add_node("analyst", analyst_node)
workflow.add_node("writer", writer_node)

# Define the paths
workflow.add_conditional_edges("researcher", lambda state: "analyst")
workflow.add_conditional_edges("analyst", lambda state: "writer")
workflow.add_conditional_edges(
    "writer",
    lambda state: END if state.get("next_node") == "FINISH" else "researcher"
)

workflow.set_entry_point("researcher")
app = workflow.compile()