import streamlit as st
import requests
import pandas as pd

def show():
    st.title("Interview History")
    st.markdown("Track your mock interview progress and review past scores.")
    
    headers = {}
    if "access_token" in st.session_state:
        headers["Authorization"] = f"Bearer {st.session_state.access_token}"
        
    res = requests.get("http://127.0.0.1:8000/interview/history", headers=headers)
    
    if res.status_code == 200:
        data = res.json().get("history", [])
        if data:
            df = pd.DataFrame(data)
            
            # Format the date column nicely if it exists
            if "date" in df.columns:
                df["date"] = pd.to_datetime(df["date"]).dt.strftime('%Y-%m-%d %H:%M')
            
            # Show the progression chart
            st.subheader("Score Progress")
            
            # Since data was sorted ascending in backend, line chart will be chronological
            if "score" in df.columns:
                # We can reset index or just plot the score column
                chart_data = df[["score"]]
                st.line_chart(chart_data)
            
            st.divider()
            
            st.subheader("History Table")
            display_cols = [col for col in ["date", "question", "score"] if col in df.columns]
            if display_cols:
                st.dataframe(df[display_cols], use_container_width=True)
            else:
                st.dataframe(df, use_container_width=True)
        else:
            st.info("You haven't completed any mock interviews yet. Try one out to see your history!")
    else:
        st.error(f"Failed to fetch interview history: {res.text}")
