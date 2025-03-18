from fastapi import APIRouter, HTTPException
from services.gemini_api import get_gemini_response
from services.scraper import scrape_website
from models.schemas import ChatRequest

router = APIRouter()

@router.post("/chat")
async def chat(request: ChatRequest):
    user_message = request.message.strip()
    
    # Fetch latest website content
    website_data = scrape_website()

    # Get AI response using fresh website content
    response = get_gemini_response(user_message, website_data)
    
    return {"response": response}
