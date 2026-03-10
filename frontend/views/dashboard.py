import streamlit as st
import plotly.express as px
import pandas as pd
import requests

def show():
    
    st.title("ðŸ“Š Student Dashboard")
    
    st.markdown("Welcome to **AI Career Copilot Analytics**")
    
    # -----------------------
    # Dashboard Metrics
    # -----------------------
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("ðŸ“„ Resume Score", "78", "+5")
    
    with col2:
        st.metric("ðŸ¤– ATS Score", "72", "+3")
    
    with col3:
        st.metric("ðŸŽ¤ Interview Score", "65", "+8")
    
    st.divider()
    
    # -----------------------
    # Interview Score Trend
    # -----------------------
    
    st.subheader("ðŸ“ˆ Interview Score Trend")
    
    try:
        response = requests.get("http://localhost:8000/interview/stats")
        if response.status_code == 200 and response.json().get("history"):
            history = response.json()["history"]
            df = pd.DataFrame(history)
            if not df.empty and "date" in df.columns and "score" in df.columns:
                fig = px.line(df, x="date", y="score", title="Interview Score Trend", markers=True)
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("Not enough data to graph interview trends.")
        else:
            st.info("No interview history found.")
    except Exception as e:
        st.error(f"Failed to fetch interview stats: {e}")
    
    # -----------------------
    # Resume Improvement
    # -----------------------
    
    st.subheader("ðŸ“Š Resume Improvement")
    
    resume_data = pd.DataFrame({
        "Version": ["V1","V2","V3","V4"],
        "Score": [50,65,72,78]
    })
    
    fig2 = px.bar(
        resume_data,
        x="Version",
        y="Score",
        title="Resume Score Improvement"
    )
    
    st.plotly_chart(fig2, use_container_width=True)
    
    # -----------------------
    # Coding Practice Progress
    # -----------------------
    
    st.subheader("ðŸ“‰ Coding Practice Progress")
    
    coding_data = pd.DataFrame({
        "Day":["Day1","Day2","Day3","Day4","Day5"],
        "Problems Solved":[2,4,5,7,9]
    })
    
    fig3 = px.area(
        coding_data,
        x="Day",
        y="Problems Solved",
        title="Coding Practice Growth"
    )
    
    st.plotly_chart(fig3, use_container_width=True)
