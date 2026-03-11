import streamlit as st
import requests

def show():
    
    st.title("Career Roadmap")
    
    goal = st.text_input("Enter your target role", placeholder="e.g. Data Scientist")
    
    missing_skills = st.text_input("Enter your missing skills (separated by comma)", placeholder="e.g. Python, SQL, Machine Learning")
    
    if st.button("Generate Roadmap"):
        if not goal.strip() or not missing_skills.strip():
            st.error("Please enter both target role and missing skills.")
            return

        st.info("Generating your custom roadmap...")
        
        headers = {}
        if "access_token" in st.session_state:
            headers["Authorization"] = f"Bearer {st.session_state.access_token}"

        response = requests.post(
            "http://127.0.0.1:8000/roadmap/generate",
            json={
                "target_role": goal,
                "missing_skills": missing_skills
            },
            headers=headers
        )

        if response.status_code == 200:
            st.subheader("Your 4-Week Roadmap")
            st.write(response.json().get("roadmap", "Failed to load roadmap."))
        else:
            st.error(f"Failed to generate roadmap: {response.text}")
    
    st.divider()
    st.subheader("Job Matching Engine")
    
    skills = st.text_input("Enter your skills separated by comma")
    
    if st.button("Find Matching Jobs"):
    
        skill_list = [s.strip() for s in skills.split(",")]
    
        response = requests.post(
            "http://127.0.0.1:8000/job/match",
            json={"skills": skill_list}
        )
    
        if response.status_code == 200:
            matches = response.json().get("matches", [])
            for job in matches:
                st.write(job["role"], f"**{job['match']}% match**")
        else:
            st.error("Failed to match jobs.")
