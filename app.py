# app.py
import streamlit as st
import os
from dotenv import load_dotenv
from graph import app  # Importing your compiled LangGraph workflow

# Load environment variables
load_dotenv()

# App Page Configurations
st.set_page_config(page_title="AeroMind AI", page_icon="🧠", layout="wide")

st.title("🧠 AeroMind: Enterprise Market Intelligence System")
st.markdown("---")

# Setup layout columns
col1, col2 = st.columns([1, 2])

with col1:
    st.header("Control Panel")
    st.write("Input your market intelligence target below. The autonomous multi-agent system will coordinate research, analysis, and execution tasks.")
    
    
    # User inputs target query
    target_query = st.text_input(
        "Market Research Objective:", 
        value="project by r rajkumar padmanabhan"
    )
    
    start_btn = st.button("Launch Autonomous Agents", type="primary")

with col2:
    st.header("Agent Execution Matrix & Output")
    
    if start_btn:
        if not os.environ.get("GROQ_API_KEY"):
            st.error("Missing GROQ_API_KEY inside your .env file!")
        else:
            # Create a live visual status bar
            status_box = st.empty()
            
            # Phase 1: Researcher Node
            status_box.status("🕵️‍♂️ [Agent Handoff] Activating Researcher Agent... Pinged Web Search Engine.")
            initial_state = {
                "task_objective": target_query,
                "plan": [],
                "messages": [],
                "next_node": ""
            }
            
            # Execute entire Graph Workflow
            with st.spinner("Agents are collaborating and synthesizing data streams..."):
                final_output = app.invoke(initial_state)
            
            status_box.success("🎯 Multi-Agent Execution Chain Completed Successfully!")
            
            # Display Final Markdown Report
            st.markdown("### 📊 Final Intelligence Brief")
            final_report = final_output["messages"][-1].content
            st.markdown(final_report)
            
            # Add an option to download the final report asset
            st.download_button(
                label="Download Intelligence Dossier (.md)",
                data=final_report,
                file_name="market_intelligence_report.md",
                mime="text/markdown"
            )