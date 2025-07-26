from langchain_core.messages import HumanMessage
from src.State.BlogState import BlogState,Blog


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

    def translation(self,state:BlogState):
        """
        translate the content of the blog to the language
        """
        prompt="""
        Translate the following blog content to {language}:
        -maintain the original tone and formatting
        -adapt cultural references and idioms to be appropriate.

        ORIGINAL CONTENT:
        {content}
        """
        blog_content=state["blog"]["content"]
        message=[
            HumanMessage(prompt.format(language=state["current_language"],content=blog_content))
        ]
        content=self.llm.with_structured_output(Blog).invoke(message)
        
    
    def route(self,state:BlogState):
        return {"current_language":state["current_language"]}

    def route_decision(self,state:BlogState):

        if state["current_language"]=="hindi":
            return "hindi_translation"
        elif state["current_language"]=="french":
            return "french_translation"
        else:
            return "hindi_translation"