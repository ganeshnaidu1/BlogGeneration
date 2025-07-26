import uvicorn
import os
from fastapi import FastAPI
from src.Graph.graph_builder import GraphBuilder
from src.LLms.GroqLLm import GroqLLm
from fastapi import Request
from dotenv import load_dotenv
load_dotenv()
app=FastAPI()
os.environ["LANGSMITH_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")


@app.post("/blogs")
async def create_blog(request:Request):
    data=await request.json()
    topic=data.get("topic")

    groqllm=GroqLLm()
    llm=groqllm.get_llm()
    
    if llm is None:
        return {"error": "Failed to initialize LLM. Please check your GROQ_API_KEY environment variable."}

    graph_builder=GraphBuilder(llm)
    if topic:
        current_language = data.get("current_language", "").lower()
        if current_language in ["hindi", "french"]:
            graph=graph_builder.set_up_graph("language").compile()
            result=graph.invoke({"topic":topic,"current_language":current_language})
            print(f"Language graph result: {result}")
            # Extract the final blog content from the result
            if isinstance(result, dict) and "blog" in result:
                return result
            else:
                return {"error": "Unexpected result format", "result": result}
        else:   
            graph=graph_builder.set_up_graph("title_generation in english").compile()
            result=graph.invoke({"topic":topic})
            print(f"English graph result: {result}")
            # Extract the final blog content from the result
            if isinstance(result, dict) and "blog" in result:
                return result
            else:
                return {"error": "Unexpected result format", "result": result}
    else:
        return {"error":"Topic is required"}

if __name__=="__main__":
    uvicorn.run(app,host="0.0.0.0",port=8000)
