from fastapi import APIRouter, HTTPException
from services.gemini_api import get_gemini_response
from models.schemas import ChatRequest

router = APIRouter()

@router.post("/chat")
async def chat(request: ChatRequest):
    user_message = request.message.strip()
    website_data = router.app.state.website_data  # Get data from app state
    response = get_gemini_response(user_message, website_data)
    return {"response": response}

