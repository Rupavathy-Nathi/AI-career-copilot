import streamlit as st

st.header("🔐 Login")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    st.success("Login functionality coming soon!")