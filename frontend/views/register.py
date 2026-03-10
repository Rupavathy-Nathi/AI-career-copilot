import streamlit as st

def show():
    
    st.header("ðŸ“ Register")
    
    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    if st.button("Register"):
        st.success("Account created (placeholder)")
