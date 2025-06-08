import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

SYSTEM_PROMPT = (
    "You are a friendly, helpful customer support assistant for an online bookstore. "
    "Answer customer questions clearly and concisely. If the user asks unrelated or unethical questions, "
    "politely decline. Be professional and concise."
)

def get_gemini_response(chat_history, user_input):
    messages = [{"role": "user", "parts": [SYSTEM_PROMPT]}]
    for pair in chat_history:
        messages.append({"role": "user", "parts": [pair["user"]]})
        messages.append({"role": "model", "parts": [pair["bot"]]})
    messages.append({"role": "user", "parts": [user_input]})

    response = model.generate_content(messages)
    return response.text