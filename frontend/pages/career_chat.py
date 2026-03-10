import streamlit as st
import requests

st.title("💬 AI Career Chat")

prompt = st.chat_input("Ask your career question")

if prompt:

    response = requests.post(
        "http://localhost:8000/chat",
        json={"message": prompt}
    )

    if response.status_code == 200:
        st.write(response.json()["reply"])
    else:
        st.error("Failed to get a response from the chat assistant.")
