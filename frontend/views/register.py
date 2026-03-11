import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

def show():
    
    st.header("Register")
    
    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    role = st.selectbox("Role", ["student", "admin"])
    
    if st.button("Register"):
        res = requests.post(
            f"{API_URL}/register",
            json={
                "name": name,
                "email": email,
                "password": password,
                "role": role
            }
        )

        if res.status_code == 200:
            st.success("Registration successful")
        else:
            st.error(res.text)
