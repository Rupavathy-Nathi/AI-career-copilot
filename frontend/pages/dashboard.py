import streamlit as st
import plotly.express as px
import pandas as pd

st.title("📊 Student Dashboard")

st.markdown("Welcome to **AI Career Copilot Analytics**")

# -----------------------
# Dashboard Metrics
# -----------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📄 Resume Score", "78", "+5")

with col2:
    st.metric("🤖 ATS Score", "72", "+3")

with col3:
    st.metric("🎤 Interview Score", "65", "+8")

st.divider()

# -----------------------
# Interview Score Trend
# -----------------------

st.subheader("📈 Interview Score Trend")

data = pd.DataFrame({
    "Interview": [1,2,3,4,5],
    "Score": [40,55,60,63,65]
})

fig = px.line(
    data,
    x="Interview",
    y="Score",
    markers=True,
    title="Interview Improvement"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------
# Resume Improvement
# -----------------------

st.subheader("📊 Resume Improvement")

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

st.subheader("📉 Coding Practice Progress")

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