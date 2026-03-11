import streamlit as st
import requests
import pandas as pd

def show():
    st.title("Question Management")
    st.markdown("Manage custom interview questions for the platform.")
    
    headers = {}
    if "access_token" in st.session_state:
        headers["Authorization"] = f"Bearer {st.session_state.access_token}"

    st.subheader("Add New Question")
    new_q = st.text_input("Enter question", placeholder="e.g. Explain polymorphism in Java")
    
    if st.button("Add Question"):
        if new_q.strip():
            res = requests.post("http://127.0.0.1:8000/admin/questions", json={"question": new_q}, headers=headers)
            if res.status_code == 200:
                st.success("Question added successfully!")
                st.rerun()
            else:
                st.error("Failed to add question")
        else:
            st.warning("Please enter a question.")
            
    st.divider()
    st.subheader("Existing Questions")
    
    res = requests.get("http://127.0.0.1:8000/admin/questions", headers=headers)
    if res.status_code == 200:
        questions = res.json().get("questions", [])
        if questions:
            for q in questions:
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.write(q["question"])
                with col2:
                    if st.button("Delete", key=f"del_{q['id']}"):
                        del_res = requests.delete(f"http://127.0.0.1:8000/admin/questions/{q['id']}", headers=headers)
                        if del_res.status_code == 200:
                            st.success("Deleted!")
                            st.rerun()
                        else:
                            st.error("Failed to delete")
        else:
            st.info("No questions listed.")
    else:
        st.error(f"Failed to load questions: {res.text}")
