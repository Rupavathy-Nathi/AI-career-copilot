import streamlit as st
from streamlit_option_menu import option_menu

def sidebar():
    pass

    with st.sidebar:
        selected = option_menu(
            "AI Career Copilot",
            [
                "Dashboard",
                "Resume Analyzer",
                "JD Analyzer",
                "Mock Interview",
                "Coding Practice",
                "Career Roadmap",
                "Profile",
                "Admin Dashboard",
                "Voice Interview"
            ],
            icons=[
                "speedometer",
                "file-earmark-text",
                "search",
                "mic",
                "code",
                "map",
                "person",
                "gear",
                "mic-fill"
            ],
            menu_icon="robot",
            default_index=0,
        )
        
        st.sidebar.markdown("---")
        st.sidebar.caption("Built with FastAPI + Streamlit + AI")
        
    return selected