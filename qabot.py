from textblob import TextBlob
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
API_TOKEN = os.getenv("HF_API_KEY")

API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"
HEADERS = {"Authorization": f"Bearer {API_TOKEN}"}

CONTEXT = """
India is a country in South Asia. Its capital city is New Delhi. It has 28 states and 8 union territories.
It is the second-most populous country in the world. India is known for its diverse cultures, languages, and religions.
The official languages are Hindi and English, but there are over 20 major languages spoken across the country.
Famous landmarks include the Taj Mahal, Qutub Minar, Red Fort, and India Gate. India has a democratic government.
The national currency is the Indian Rupee (INR). The country celebrates many festivals like Diwali, Holi, Eid, and Christmas.
"""

def ask_question(question):
    payload = {
        "inputs": {
            "question": question,
            "context": CONTEXT
        }
    }
    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        if response.status_code == 200:
            return response.json().get("answer", "No answer found.")
        else:
            return "Error: " + response.text
    except Exception as e:
        return f"Something went wrong: {e}"

print("🤖 AI Q&A Bot (type 'exit' to quit)")
while True:
    user_q = input("You: ")
    if user_q.lower() == "exit":
        break

    # Correct spelling silently
    corrected_q = str(TextBlob(user_q).correct())
    answer = ask_question(corrected_q)
    print("Bot:", answer)