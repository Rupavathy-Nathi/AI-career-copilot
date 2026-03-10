import streamlit as st
import requests

st.title("🔐 Login")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):

    response = requests.post(
        "http://localhost:8000/login",
        json={
            "email": email,
            "password": password
        }
    )

    if response.status_code == 200:

        data = response.json()

        st.session_state.logged_in = True
        st.session_state.role = data["role"]

        st.success("Login successful")
        st.rerun()

    else:
        st.error("Invalid credentials")