import streamlit as st
import requests

def show():
    
    st.title("Job Description Analyzer")
    
    jd = st.text_area(
        "Paste Job Description",
        height=200
    )
    
    if st.button("Analyze JD"):
        if not jd.strip():
            st.error("Please paste a job description first.")
            return
            
        st.info("Analyzing job description...")
        
        headers = {}
        if "access_token" in st.session_state:
            headers["Authorization"] = f"Bearer {st.session_state.access_token}"

        response = requests.post(
            "http://127.0.0.1:8000/job/analyze",
            json={"job_description": jd},
            headers=headers
        )

        if response.status_code == 200:
            st.subheader("Analysis Results")
            st.write(response.json().get("analysis", "No analysis returned."))
        else:
            st.error(f"Failed to analyze JD: {response.text}")
