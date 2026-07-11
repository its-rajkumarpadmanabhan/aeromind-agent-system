# main.py
import os
from graph import app

if __name__ == "__main__":
    # Ensure an API key exists before firing up the engines
    if not os.environ.get("GROQ_API_KEY"):
        print("CRITICAL ERROR: Please add your GROQ_API_KEY to your .env file!")
        exit(1)

    initial_input = {
        "task_objective": "What are the latest major market updates regarding NVIDIA's AI chips?",
        "plan": [],
        "messages": [],
        "next_node": ""
    }
    
    print("Starting Multi-Agent Execution...")
    final_state = app.invoke(initial_input)
    
    print("\n==================================================")
    print("       FINAL GENERATED INTELLIGENCE REPORT        ")
    print("==================================================")
    # The last message in the list comes from our Executive Writer
    print(final_state["messages"][-1].content)