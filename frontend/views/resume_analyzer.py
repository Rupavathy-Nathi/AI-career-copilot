import streamlit as st
import requests

def show():
    
    st.title("ðŸ“„ Resume Analyzer")
    
    st.write("Upload your resume to analyze ATS score and improvements.")
    
    resume = st.file_uploader(
        "Upload Resume",
        type=["pdf","docx"]
    )
    
    if resume:
        st.success("Resume uploaded successfully!")
        
        # We will simulate reading the resume text here
        resume_text = "Simulated resume text content based on upload."
    
        if st.button("Analyze Resume"):
            st.info("Analyzing resume...")
    
        if st.button("Improve Resume with AI"):
    
            response = requests.post(
                "http://localhost:8000/resume/improve",
                json={"content": resume_text}
            )
    
            st.subheader("AI Improved Resume")
    
            if response.status_code == 200:
                st.write(response.json()["improved_resume"])
            else:
                st.error("Failed to generate improvements.")
