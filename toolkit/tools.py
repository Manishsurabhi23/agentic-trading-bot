# from langchain.tools import tool
# from pydantic import BaseModel
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from lancedb.rerankers import LinearCombinationReranker
# from langchain_community.vectorstores import LanceDB
# from langchain_community.tools import TavilySearchResults
# from langchain_community.tools.polygon.financials import PolygonFinancials
# from langchain_community.utilities.polygon import PolygonAPIWrapper
# from langchain_community.tools.bing_search import BingSearchResults
# from config.config_loader import load_config
# from data_models.models import RagToolSchema

# config = load_config()  # Load the config at the module level 
# #print("loaded all dependencies successfully")

# @tool(args_schema=RagToolSchema)
# def retriever_tool(question):
#     return "<no_need_to_know>"
# @tool
# def tavily_tool(question:str):
#     """Tool to perform Tavily search for a given question."""
#     tavily_search = TavilySearchResults(
#         question,
#         max_results = 5,
#         search_depth="advanced",
#         include_answer=True,
#         include_raw_content=True,
#         api_key=config.TAVILY_API_KEY)
#     return tavily_search.run(question)
# @tool
# def create_polygon_tool():
#     """Tool to fetch financial data using Polygon API."""
#     return PolygonFinancials(api_wrapper=PolygonAPIWrapper(api_key=config.POLYGON_API_KEY))

# @tool
# def bing_search_tool(query:str):
#     """Tool to perform Bing search for a given query."""
#     bing_tool = BingSearchResults(
#         query,
#         max_results = 5,
#         include_answer=True,
#         include_raw_content=True,
#         api_key=config.BING_API_KEY)
#     return bing_tool.run(query)

# #print("defined all tools successfully")
# def get_all_tools(question):
#     """Function to get all defined tools."""
#     tools = [
#         retriever_tool(question),
#         tavily_tool,
#         create_polygon_tool(),
#         bing_search_tool
#     ]
#     return tools


# if __name__ == "__main__":
#     tools = get_all_tools("What is the latest stock price of Apple?")
#     for tool in tools:
#         print(tool)

import os
from langchain.tools import tool
from langchain_community.tools import TavilySearchResults
from langchain_community.tools.polygon.financials import PolygonFinancials
from langchain_community.utilities.polygon import PolygonAPIWrapper
from langchain_community.tools.bing_search import BingSearchResults 
from data_models.models import RagToolSchema
from langchain_pinecone import PineconeVectorStore
from utils.model_loaders import ModelLoader
from utils.config_loader import load_config
from dotenv import load_dotenv
from pinecone import Pinecone
load_dotenv()
api_wrapper = PolygonAPIWrapper()
model_loader=ModelLoader()
config = load_config()

@tool(args_schema=RagToolSchema)
def retriever_tool(question):
    """this is retriever tool"""
    pinecone_api_key = os.getenv("PINECONE_API_KEY")
    pc = Pinecone(api_key=pinecone_api_key)
    vector_store = PineconeVectorStore(index=pc.Index(config["vector_db"]["index_name"]), 
                            embedding= model_loader.load_embeddings())
    retriever = vector_store.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={"k": config["retriever"]["top_k"] , "score_threshold": config["retriever"]["score_threshold"]},
    )
    retriever_result=retriever.invoke(question)
    
    return retriever_result

tavilytool = TavilySearchResults(
    max_results=config["tools"]["tavily"]["max_results"],
    search_depth="advanced",
    include_answer=True,
    include_raw_content=True,
    )

financials_tool = PolygonFinancials(api_wrapper=api_wrapper)