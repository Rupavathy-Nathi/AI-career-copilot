import streamlit as st

st.title("🎤 AI Mock Interview")

role = st.selectbox(
    "Select Interview Role",
    [
        "Software Engineer",
        "Data Analyst",
        "Machine Learning Engineer"
    ]
)

difficulty = st.selectbox(
    "Difficulty",
    ["Easy","Medium","Hard"]
)

if st.button("Start Interview"):
    st.success("Interview starting...")