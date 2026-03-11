import streamlit as st
import requests

def show():
    
    st.title("Coding Practice")
    
    topic = st.text_input("Topic", placeholder="e.g. Binary Trees, Dynamic Programming")
    
    difficulty = st.selectbox(
        "Select Difficulty",
        ["Easy","Medium","Hard"]
    )
    
    if st.button("Generate Coding Question"):
        if not topic.strip():
            st.error("Please enter a topic first.")
            return

        st.info("Generating question...")
        
        headers = {}
        if "access_token" in st.session_state:
            headers["Authorization"] = f"Bearer {st.session_state.access_token}"

        response = requests.post(
            "http://127.0.0.1:8000/coding/generate",
            json={
                "topic": topic,
                "difficulty": difficulty
            },
            headers=headers
        )

        if response.status_code == 200:
            st.subheader("Your Coding Problem")
            # Groq model return key is 'problem'
            st.write(response.json().get("problem", "No problem generated."))
        else:
            st.error(f"Failed to generate problem: {response.text}")
