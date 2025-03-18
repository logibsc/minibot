import os
import uvicorn
from fastapi import FastAPI, HTTPException
from services.scraper import scrape_website
from services.gemini_api import get_gemini_response
from services.memory import ConversationMemory
from models.schemas import ChatRequest, ChatResponse

# ✅ Initialize FastAPI
app = FastAPI(title="Floating Chatbot", version="1.0")

# ✅ Set website URL
WEBSITE_URL = "https://alphaesai.com"

# ✅ Initialize conversation memory
conversation_memory = ConversationMemory()

# ✅ Ensure GEMINI_API_KEY is set
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("⚠️ GEMINI_API_KEY is missing! Set it in Railway's environment variables.")

@app.on_event("startup")
async def load_website_data():
    """Fetch website content at startup without breaking the app."""
    try:
        print("🔄 Scraping website data...")
        app.state.website_data = scrape_website(WEBSITE_URL)
        print("✅ Website data loaded successfully!")
    except Exception as e:
        print(f"⚠️ Failed to scrape website: {e}")
        app.state.website_data = "Website content unavailable"

@app.get("/")
def home():
    """Health check endpoint."""
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

# ✅ Run the server on the correct Railway port
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Defaults to 8000 if not set
    uvicorn.run(app, host="0.0.0.0", port=port)
