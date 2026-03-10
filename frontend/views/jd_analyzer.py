import streamlit as st

def show():
    
    st.title("Job Description Analyzer")
    
    jd = st.text_area(
        "Paste Job Description",
        height=200
    )
    
    if st.button("Analyze JD"):
        st.info("Analyzing job description...")
