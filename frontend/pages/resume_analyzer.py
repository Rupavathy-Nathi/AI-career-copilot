import streamlit as st

st.title("📄 Resume Analyzer")

st.write("Upload your resume to analyze ATS score and improvements.")

resume = st.file_uploader(
    "Upload Resume",
    type=["pdf","docx"]
)

if resume:
    st.success("Resume uploaded successfully!")

    if st.button("Analyze Resume"):
        st.info("Analyzing resume...")