from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt.tool_node import ToolNode , tool_condition
from langchain_core.messages import AIMessage, HumanMessage
from typing_extensions import Annotated, TypedDict
from utils.model_loaders import ModelLoader
from toolkit.tools import get_all_tools
class State(TypedDict):
    
    messages: Annotated[List,add_messages]

class GraphBuilder:
    def __init__(self, *args, **kwds):
        pass
    def _chatbot_node(self,state:State):
        pass
    def build():
        pass
    def get_graph(self):
        pass