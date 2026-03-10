import streamlit as st

def show():
    
    st.title("ðŸ’» Coding Practice")
    
    difficulty = st.selectbox(
        "Select Difficulty",
        ["Easy","Medium","Hard"]
    )
    
    if st.button("Generate Coding Question"):
        st.info("Generating question...")
