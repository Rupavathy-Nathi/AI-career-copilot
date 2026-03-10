import streamlit as st

st.set_page_config(page_title="AI Career Copilot", layout="wide")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "role" not in st.session_state:
    st.session_state.role = None

st.title("🚀 AI Career Copilot")
st.caption("AI-powered placement preparation platform")

# -------------------------
# BEFORE LOGIN
# -------------------------
if not st.session_state.logged_in:

    page = st.sidebar.selectbox(
        "Menu",
        ["Login", "Register"]
    )

    if page == "Login":
        from views import login
        login.show()

    if page == "Register":
        from views import register
        register.show()

# -------------------------
# AFTER LOGIN
# -------------------------
else:
    menu = [
        "Dashboard",
        "Resume Analyzer",
        "JD Analyzer",
        "Mock Interview",
        "Coding Practice",
        "Career Roadmap",
        "Career Chat",
        "Voice Interview",
        "Profile"
    ]

    if st.session_state.role == "admin":
        menu.append("Admin Dashboard")

    menu.append("Logout")

    page = st.sidebar.selectbox("Menu", menu)

    st.sidebar.markdown("---")
    st.sidebar.caption("Built with FastAPI + Streamlit + AI")

    if page == "Dashboard":
        from views import dashboard
        dashboard.show()

    elif page == "Resume Analyzer":
        from views import resume_analyzer
        resume_analyzer.show()

    elif page == "JD Analyzer":
        from views import jd_analyzer
        jd_analyzer.show()

    elif page == "Mock Interview":
        from views import mock_interview
        mock_interview.show()

    elif page == "Coding Practice":
        from views import coding_practice
        coding_practice.show()

    elif page == "Career Roadmap":
        from views import career_roadmap
        career_roadmap.show()

    elif page == "Career Chat":
        from views import career_chat
        career_chat.show()

    elif page == "Voice Interview":
        from views import voice_interview
        voice_interview.show()

    elif page == "Profile":
        from views import profile
        profile.show()

    elif page == "Admin Dashboard":
        from views import admin_dashboard
        admin_dashboard.show()

    elif page == "Logout":
        st.session_state.logged_in = False
        st.session_state.role = None
        st.success("Logged out successfully")
        st.rerun()