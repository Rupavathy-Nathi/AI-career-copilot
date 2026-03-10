import streamlit as st

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "role" not in st.session_state:
    st.session_state.role = None

st.set_page_config(
    page_title="AI Career Copilot",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 AI Career Copilot")
st.caption("AI-powered placement preparation platform")

if not st.session_state.logged_in:

    page = st.sidebar.selectbox(
        "Menu",
        ["Login", "Register"]
    )

else:

    menu = [
        "Dashboard",
        "Resume Analyzer",
        "JD Analyzer",
        "Mock Interview",
        "Coding Practice",
        "Career Roadmap",
        "Voice Interview",
        "Career Chat",
        "Profile"
    ]

    # Admin access
    if st.session_state.role == "admin":
        menu.append("Admin Dashboard")

    menu.append("Logout")

    page = st.sidebar.selectbox("Menu", menu)

st.sidebar.markdown("---")
st.sidebar.caption("Built with FastAPI + Streamlit + AI")

if page == "Logout":

    st.session_state.logged_in = False
    st.session_state.role = None

    st.success("Logged out successfully")

    st.rerun()

if page == "Login":
    import pages.login

elif page == "Register":
    import pages.register

elif page == "Dashboard":
    import pages.dashboard

elif page == "Resume Analyzer":
    import pages.resume_analyzer

elif page == "JD Analyzer":
    import pages.jd_analyzer

elif page == "Mock Interview":
    import pages.mock_interview

elif page == "Coding Practice":
    import pages.coding_practice

elif page == "Career Roadmap":
    import pages.career_roadmap

elif page == "Voice Interview":
    import pages.voice_interview

elif page == "Career Chat":
    import pages.career_chat

elif page == "Profile":
    import pages.profile

elif page == "Admin Dashboard":
    import pages.admin_dashboard