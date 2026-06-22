import streamlit as st
from groq import Groq

# 1. Read the key safely from Streamlit's Secrets manager
try:
    api_key = st.secrets["GROQ_API_KEY"]
except KeyError:
    st.error("GROQ_API_KEY is missing from Streamlit Secrets! Please check your dashboard setup.")
    st.stop()

# 2. Pass the key explicitly to the Groq client instance
client = Groq(api_key=api_key)

def ask_llm(prompt):
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=512
    )
    return response.choices[0].message.content