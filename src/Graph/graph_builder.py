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

    def build_language_graph(self):
        """
        Build the graph for blog generation with inputs topics and language
        """
        self.blog_node=BlogNode(self.llm)
        self.graph_builder.add_node("title_generator",self.blog_node.title_creation)
        self.graph_builder.add_node("content_generator",self.blog_node.content_creation)
        self.graph_builder.add_node("route",self.blog_node.route)
        self.graph_builder.add_node("hindi_translation",lambda state:self.blog_node.translation({**state,"current_language":"hindi"}))
        self.graph_builder.add_node("french_translation",lambda state:self.blog_node.translation({**state,"current_language":"french"}))
        self.graph_builder.add_edge(START, "title_generator")
        self.graph_builder.add_edge("title_generator", "content_generator")
        self.graph_builder.add_edge("content_generator", "route")
        
        self.graph_builder.add_conditional_edges(
            "route",
            self.blog_node.route_decision,
            {
                "hindi_translation":"hindi_translation",
                "french_translation":"french_translation"
            }
        )
        self.graph_builder.add_edge("hindi_translation",END)
        self.graph_builder.add_edge("french_translation",END)
        return self.graph_builder

    def get_graph(self):
        return self.graph_builder

    def set_up_graph(self,usecase):
        if usecase=="title_generation in english":
            return self.build_graph()
        if usecase=="language":
            return self.build_language_graph()