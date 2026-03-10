import streamlit as st

st.title("🧭 Career Roadmap")

goal = st.text_input(
    "Enter your target role"
)

if st.button("Generate Roadmap"):
    st.success("Generating roadmap...")