import streamlit as st
import requests
import pandas as pd

def show():
    st.title("Resume Scores")
    st.markdown("Monitor student resume analysis scores.")
    
    headers = {}
    if "access_token" in st.session_state:
        headers["Authorization"] = f"Bearer {st.session_state.access_token}"
        
    res = requests.get("http://127.0.0.1:8000/admin/resumes", headers=headers)
    
    if res.status_code == 200:
        data = res.json().get("resumes", [])
        if data:
            df = pd.DataFrame(data)
            if "student" in df.columns and "score" in df.columns:
                st.dataframe(df[["student", "score", "date"]], use_container_width=True)
            else:
                st.dataframe(df, use_container_width=True)
        else:
            st.info("No resume scores available yet.")
    else:
        st.error(f"Failed to fetch resume scores: {res.text}")
