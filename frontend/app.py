import streamlit as st

from components.sidebar import sidebar

st.set_page_config(
    page_title="AI Career Copilot",
    page_icon="🚀",
    layout="wide"
)

selected = sidebar()

if selected == "Dashboard":
    import pages.dashboard

elif selected == "Resume Analyzer":
    import pages.resume_analyzer

elif selected == "JD Analyzer":
    import pages.jd_analyzer

elif selected == "Mock Interview":
    import pages.mock_interview

elif selected == "Coding Practice":
    import pages.coding_practice

elif selected == "Career Roadmap":
    import pages.career_roadmap

elif selected == "Profile":
    import pages.profile

elif selected == "Admin Dashboard":
    import pages.admin_dashboard

elif selected == "Voice Interview":
    import pages.voice_interview