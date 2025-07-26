from src.State.BlogState import BlogState


class BlogNode:
    def __init__(self,llm):
        self.llm=llm

    def title_creation(self,state:BlogState):
        """
        create the title of the blog
        """
        if "topic" in state and state["topic"]:
            prompt="""
            Generate a single, creative, and SEO-friendly blog title for the topic: {topic}
            
            Requirements:
            - Return ONLY the title, nothing else
            - No explanations, no multiple options
            - Keep it under 60 characters
            - Make it engaging and click-worthy
            
            Title:
            """
            system_prompt=prompt.format(topic=state["topic"])
            response=self.llm.invoke(system_prompt)
            return {"blog":{"title":response.content.strip()}}

    def content_creation(self,state:BlogState):
        """
        create the content of the blog
        """
        if "topic" in state and state["topic"]:
            prompt="""
            Write a comprehensive blog post about: {topic}
            
            Requirements:
            - Use proper Markdown formatting
            - Include an introduction, main sections with headers, and conclusion
            - Write 800-1200 words
            - Make it informative and engaging
            - Include relevant examples and insights
            - No meta-commentary or explanations about the writing process
            
            Blog content:
            """
            system_prompt=prompt.format(topic=state["topic"])
            response=self.llm.invoke(system_prompt)
            return {"blog":{"title":state["blog"]["title"],"content":response.content.strip()}}