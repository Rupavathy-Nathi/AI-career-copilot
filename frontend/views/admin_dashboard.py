import streamlit as st
import pandas as pd
import plotly.express as px

def show():
    
    st.title("Admin Dashboard")
    
    st.markdown("Platform analytics and user management")
    
    # ----------------------
    # Platform Metrics
    # ----------------------
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Users", "120")
    
    with col2:
        st.metric("Total Interviews", "340")
    
    with col3:
        st.metric("Average Resume Score", "74")
    
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
