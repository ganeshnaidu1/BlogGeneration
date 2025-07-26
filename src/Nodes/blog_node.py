from State.BlogState import BlogState


class BlogNode:
    def __init__(self,llm):
        self.llm=llm

    def title_creation(self,state:BlogState):
        return self.llm.generate_blog(BlogState.topic)