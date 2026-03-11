import streamlit as st
import requests

def show():
    
    st.title("Voice Mock Interview")
    
    question = st.text_area("Interview Question", placeholder="e.g. Explain polymorphism in Java")
    
    audio_bytes = st.audio_input("Record your answer")
    
    if audio_bytes:
        if not question.strip():
            st.error("Please enter an interview question before recording.")
            return
    
        files = {"audio": ("audio.wav", audio_bytes.getvalue())}
        data = {"question": question}
    
        headers = {}
        if "access_token" in st.session_state:
            headers["Authorization"] = f"Bearer {st.session_state.access_token}"

        res = requests.post(
            "http://127.0.0.1:8000/voice/interview",
            files=files,
            data=data,
            headers=headers
        )
    
        if res.status_code == 200:
            result = res.json()
            if "transcribed_text" in result:
                st.subheader("Your Answer (Transcribed):")
                st.write(result["transcribed_text"])
                
                st.subheader("Score:")
                st.write(f"**{result.get('score', 0)}/100**")
                
                st.subheader("Feedback:")
                st.write(result.get("feedback", "No feedback available."))
                
                st.subheader("Ideal Answer:")
                st.write(result.get("ideal_answer", "No ideal answer available."))
                
                suggestions = result.get("suggestions", [])
                if suggestions:
                    st.subheader("Suggestions:")
                    for s in suggestions:
                        st.write("•", s)
            else:
                st.error(result.get("error", "Failed to parse audio."))
        else:
            st.error(f"Voice Server Offline: {res.text}")
