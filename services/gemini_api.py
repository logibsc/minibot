import os
import google.generativeai as genai

# Load API Key from system environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Ensure API key is set
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in the system environment variables.")

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

def get_gemini_response(user_message, chat_history, website_data):
    """Calls Gemini 1.5 Pro API to generate a response."""

    # Ensure user_message is valid
    if not user_message.strip():
        return "Please provide a valid input."

    prompt = (
        f"You are an AI chatbot for the website {website_data}. "
        f"Answer based on the website content.\n\n"
        f"User: {user_message}\n"
        f"Previous Context: {chat_history}\n\n"
        f"Answer:"
    )

    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(prompt)

        # Handle response properly
        if response and hasattr(response, "text"):
            return response.text.strip()
        else:
            return "I'm not sure about that."

    except Exception as e:
        return f"Error: {str(e)}"
