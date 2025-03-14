import os
from fastapi import FastAPI, HTTPException, Depends
from services.scraper import scrape_website
from services.gemini_api import get_gemini_response
from services.memory import ConversationMemory
from models.schemas import ChatRequest, ChatResponse

# Initialize FastAPI
app = FastAPI(title="Floating Chatbot", version="1.0")

# Set website URL
WEBSITE_URL = "https://alphaesai.com"

# Scrape website at startup
app.state.website_data = scrape_website(WEBSITE_URL)

# Initialize conversation memory
conversation_memory = ConversationMemory()

@app.get("/")
def home():
    return {"message": "Welcome to the Floating Chatbot!", "status": "running"}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Handles chatbot queries and returns AI-generated responses."""
    
    user_message = request.message.strip()
    if not user_message:
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    # Get previous conversation context
    chat_history = conversation_memory.get_summary()

    # Get AI response using Gemini API
    response = get_gemini_response(user_message, chat_history, app.state.website_data)

    # Store the conversation in memory
    conversation_memory.add_message(user_message, response)

    return {"response": response}
