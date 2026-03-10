import streamlit as st

st.title("💻 Coding Practice")

difficulty = st.selectbox(
    "Select Difficulty",
    ["Easy","Medium","Hard"]
)

if st.button("Generate Coding Question"):
    st.info("Generating question...")