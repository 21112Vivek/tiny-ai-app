import streamlit as st
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
    """
    Sends the question to the Hugging Face model and returns the answer.
    """
    payload = {
        "inputs": {
            "question": str(TextBlob(question).correct()),  # silent spell correction
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

# Streamlit UI
st.title("🤖 Tiny AI Q&A Bot")
st.write("Ask a question about India and get an answer!")

user_question = st.text_input("Type your question here:")

if st.button("Get Answer"):
    if user_question.strip() == "":
        st.warning("Please enter a question first.")
    else:
        answer = ask_question(user_question)
        st.success(f"Bot: {answer}")