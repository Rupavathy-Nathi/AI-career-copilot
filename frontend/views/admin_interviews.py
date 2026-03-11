import streamlit as st
import requests
import pandas as pd

def show():
    st.title("Interview Results")
    st.markdown("Monitor student interview scores and performance.")
    
    headers = {}
    if "access_token" in st.session_state:
        headers["Authorization"] = f"Bearer {st.session_state.access_token}"
        
    res = requests.get("http://127.0.0.1:8000/admin/interviews", headers=headers)
    
    if res.status_code == 200:
        data = res.json().get("interviews", [])
        if data:
            df = pd.DataFrame(data)
            # Assuming columns: student, question, score, date
            if "student" in df.columns and "question" in df.columns and "score" in df.columns:
                st.dataframe(df[["student", "question", "score", "date"]], use_container_width=True)
            else:
                st.dataframe(df, use_container_width=True)
        else:
            st.info("No interview results available yet.")
    else:
        st.error(f"Failed to fetch interview results: {res.text}")
