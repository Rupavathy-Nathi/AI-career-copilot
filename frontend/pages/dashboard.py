import streamlit as st

st.title("📊 Student Dashboard")

st.markdown("Welcome to **AI Career Copilot** — your placement preparation assistant.")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="📄 Resume Score",
        value="78",
        delta="+5 improvement"
    )

with col2:
    st.metric(
        label="🤖 ATS Score",
        value="72",
        delta="+3 improvement"
    )

with col3:
    st.metric(
        label="🎤 Interview Score",
        value="65",
        delta="+8 improvement"
    )

st.divider()

st.subheader("🔥 Quick Actions")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Analyze Resume"):
        st.info("Navigate to Resume Analyzer")

with col2:
    if st.button("Start Mock Interview"):
        st.info("Navigate to Mock Interview")

with col3:
    if st.button("Practice Coding"):
        st.info("Navigate to Coding Practice")