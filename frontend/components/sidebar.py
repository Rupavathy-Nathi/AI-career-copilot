import streamlit as st
from streamlit_option_menu import option_menu

def sidebar():

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
                "Profile"
            ],
            icons=[
                "speedometer",
                "file-earmark-text",
                "search",
                "mic",
                "code",
                "map",
                "person"
            ],
            menu_icon="robot",
            default_index=0,
        )

    return selected