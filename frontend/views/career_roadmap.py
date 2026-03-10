import streamlit as st
import requests

def show():
    
    st.title("Career Roadmap")
    
    goal = st.text_input(
        "Enter your target role"
    )
    
    if st.button("Generate Roadmap"):
        st.success("Generating roadmap...")
    
    st.divider()
    st.subheader("Job Matching Engine")
    
    skills = st.text_input("Enter your skills separated by comma")
    
    if st.button("Find Matching Jobs"):
    
        skill_list = [s.strip() for s in skills.split(",")]
    
        response = requests.post(
            "http://localhost:8000/job/match",
            json={"skills": skill_list}
        )
    
        if response.status_code == 200:
            matches = response.json().get("matches", [])
            for job in matches:
                st.write(job["role"], f"**{job['match']}% match**")
        else:
            st.error("Failed to match jobs.")
