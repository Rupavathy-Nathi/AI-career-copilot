import streamlit as st
import pandas as pd
import plotly.express as px

def show():
    
    st.title("Admin Dashboard")
    
    st.markdown("Platform analytics and user management")
    
    # ----------------------
    # Platform Metrics
    # ----------------------
    
    headers = {}
    if "access_token" in st.session_state:
        headers["Authorization"] = f"Bearer {st.session_state.access_token}"

    try:
        import requests
        res = requests.get("http://127.0.0.1:8000/admin/stats", headers=headers)
        if res.status_code == 200:
            stats = res.json()
            users_count = stats.get("users", 0)
            interviews_count = stats.get("interviews", 0)
        else:
            users_count = "Error"
            interviews_count = "Error"
    except Exception:
        users_count = "Error"
        interviews_count = "Error"

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Users", users_count)
    
    with col2:
        st.metric("Total Interviews", interviews_count)
    
    with col3:
        st.metric("Platform Status", "Online" if users_count != "Error" else "Offline")
    
    st.divider()
    
    # ----------------------
    # Skill Gap Statistics
    # ----------------------
    
    st.subheader("Skill Gap Statistics")
    
    skill_data = pd.DataFrame({
        "Skill": ["DSA", "System Design", "SQL", "Machine Learning"],
        "Students Missing Skill": [70, 50, 40, 35]
    })
    
    fig = px.bar(
        skill_data,
        x="Skill",
        y="Students Missing Skill",
        title="Most Missing Skills"
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.divider()
    
    # ----------------------
    # User Management
    # ----------------------
    
    st.subheader("User Management")
    
    users = pd.DataFrame({
        "User ID": [1,2,3],
        "Name": ["Alice", "Bob", "Charlie"],
        "Email": ["alice@mail.com","bob@mail.com","charlie@mail.com"]
    })
    
    st.dataframe(users)
    
    user_id = st.number_input("Enter User ID to delete", min_value=1)
    
    if st.button("Delete User"):
        st.warning(f"User {user_id} deleted (demo)")
