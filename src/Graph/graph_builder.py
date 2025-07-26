from langgraph.graph import StateGraph,START,END
from State.BlogState import state
from LLms.GroqLLm import GroqLLm
from State.BlogState import BlogState
class GraphBuilder:
    def __init__(self,llm):
        self.llm=llm
        self.graph_builder=StateGraph(BlogState)

    def build_graph(self):
        """
        This is the graph builder for the blog generation graph.
        It is a state graph that uses the BlogState class to store the state of the graph.
        It uses the GroqLLm class to get the LLM.
        It uses the BlogState class to store the state of the graph.
        It uses the BlogState class to store the state of the graph.
        """
        self.graph_builder.add_node("llm",self.llm.get_llm())
        self.graph_builder.add_edge(START, "llm")
        self.graph_builder.add_edge("llm", END)
        return self.graph_builder

    def get_graph(self):
        return self.graph_builder
