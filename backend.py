from dotenv import load_dotenv
load_dotenv()

#Step1: Setup Pydantic Model (Schema Validation)
from pydantic import BaseModel
from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from ai_agent import get_response_from_ai_agent

ALLOWED_MODEL_NAMES=["llama3-70b-8192", "mixtral-8x7b-32768", "llama-3.3-70b-versatile" ]

app=FastAPI(title="LangGraph AI Agent")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="."), name="static")

@app.get("/")
async def read_root():
    return FileResponse("index.html")

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool

@app.post("/chat")
def chat_endpoint(request: RequestState): 
    """
    API Endpoint to interact with the Chatbot using LangGraph and search tools.
    It dynamically selects the model specified in the request"""

    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error":"Invalid model name . Kindly select the valid AI model"}
    
    llm_id = request.model_name 
    query = request.messages
    allow_search = request.allow_search
    system_prompt = request.system_prompt
    provider = request.model_provider

    # creating ai agent to get response from it
    response = get_response_from_ai_agent(llm_id, query , allow_search , system_prompt , provider)
    return response

# run app and explore swagger ui docs
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=9999)