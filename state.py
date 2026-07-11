from typing import Annotated, TypedDict, List
from langchain_core.messages import BaseMessage
from operator import add

class AgentState(TypedDict):
    # The original objective given by the user
    task_objective: str
    
    # Internal list of sub-tasks planned by the supervisor
    plan: List[str]
    
    # Message history: Annotated[..., add] allows nodes to append messages 
    # to the state instead of overwriting them entirely
    messages: Annotated[List[BaseMessage], add]
    
    # Tracks which node goes next ("researcher", "analyst", "writer", "FINISH")
    next_node: str