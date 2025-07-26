from langgraph.graph import StateGraph,START,END
from src.LLms.GroqLLm import GroqLLm
from src.Nodes.blog_node import BlogNode
from src.State.BlogState import BlogState,Blog
class GraphBuilder:
    def __init__(self,llm):
        self.llm=llm
        self.graph_builder=StateGraph(BlogState)

    def build_graph(self):
        """
        Build the graph for the blog generation. based on the topic
        """
        self.blog_node=BlogNode(self.llm)
        self.graph_builder.add_node("title_generator",self.blog_node.title_creation)
        self.graph_builder.add_node("content_generator",self.blog_node.content_creation)
        self.graph_builder.add_edge(START, "title_generator")
        self.graph_builder.add_edge("title_generator", "content_generator")
        self.graph_builder.add_edge("content_generator",END)
        return self.graph_builder

    def get_graph(self):
        return self.graph_builder

    def set_up_graph(self,usecase):
        if usecase=="title_generation in english":
            return self.build_graph()
        

