import streamlit as st
import requests

import PyPDF2
import docx
import io

def extract_text(file):
    text = ""
    if file.name.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    elif file.name.endswith(".docx"):
        doc = docx.Document(file)
        text = "\n".join([para.text for para in doc.paragraphs])
    else:
        # Fallback for plain text
        try:
            text = file.getvalue().decode("utf-8")
        except:
            text = "Unsupported file format or decoding error."
    return text

def show():
    
    st.title("Resume Analyzer")
    
    st.write("Upload your resume to analyze ATS score and improvements.")
    
    resume = st.file_uploader(
        "Upload Resume",
        type=["pdf","docx","txt"]
    )
    
    if resume:
        st.success("Resume uploaded successfully!")
        
        # Read the real uploaded file text
        resume_text = extract_text(resume)
    
        if st.button("Analyze Resume"):
            st.info("Analyzing resume...")
    
        if st.button("Improve Resume with AI"):
    
            response = requests.post(
                "http://127.0.0.1:8000/resume/improve",
                json={"content": resume_text}
            )
    
            st.subheader("AI Improved Resume")
    
            if response.status_code == 200:
                st.write(response.json()["improved_resume"])
            else:
                st.error("Failed to generate improvements.")
