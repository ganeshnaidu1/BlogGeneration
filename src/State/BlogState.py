from typing import TypedDict
from pydantic import BaseModel,Field


class Blog(BaseModel):
    title:str=Field(description="The title of the blog")
    description:str=Field(description="The description of the blog")

class BlogState(TypedDict):
    topic:str
    blog:Blog
    current_language:str
    