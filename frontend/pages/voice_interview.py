import streamlit as st
import requests
from streamlit_mic_recorder import mic_recorder

st.title("🎤 Voice Mock Interview")

audio = mic_recorder(start_prompt="Start Recording")

if audio:

    st.audio(audio["bytes"])

    files = {"audio": ("audio.wav", audio["bytes"])}

    res = requests.post(
        "http://localhost:8000/voice/interview",
        files=files
    )

    st.success(res.json()["transcribed_text"])