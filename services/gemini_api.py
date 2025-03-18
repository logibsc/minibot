import os
import google.generativeai as genai

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set in the system environment variables.")

genai.configure(api_key=GEMINI_API_KEY)

def get_gemini_response(user_message, chat_history, website_data):
    # Use website_data in the response generation
    """Calls Gemini 1.5 Pro API to generate a response dynamically based on website data."""

    if not user_message.strip():
        return "Please provide a valid input."

    prompt = (
        f"You are an AI chatbot for the website 'https://alphaesai.com'. "
        f"Here is the latest website content:\n{website_data}\n\n"
        f"Answer the user's question based on this information.\n\n"
        f"User: {user_message}\n\n"
        f"Answer:"
    )

    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(prompt)

        return response.text.strip() if response and hasattr(response, "text") else "I'm not sure about that."

    except Exception as e:
        return f"Error: {str(e)}"
