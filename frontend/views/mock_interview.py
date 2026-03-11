import streamlit as st
import requests
import plotly.graph_objects as go

def show():
    
    st.title("Mock Interview")
    
    question = st.text_area("Interview Question")
    
    answer = st.text_area("Your Answer")
    
    if st.button("Evaluate Answer"):
    
        headers = {}
        if "access_token" in st.session_state:
            headers["Authorization"] = f"Bearer {st.session_state.access_token}"

        response = requests.post(
            "http://127.0.0.1:8000/interview/evaluate",
            json={
                "question": question,
                "answer": answer
            },
            headers=headers
        )
    
        data = response.json()
    
        score = data.get("score", "Not available")
        st.success(f"Overall Score: {score}/100")
    
        col1, col2, col3 = st.columns(3)
    
        col1.metric("Communication", data.get("communication", 0))
        col2.metric("Technical Depth", data.get("technical_depth", 0))
        col3.metric("Confidence", data.get("confidence", 0))
    
        st.subheader("AI Suggestion")
    
        st.info(data.get("suggestion", "No suggestion available."))
    
        fig = go.Figure()
    
        fig.add_trace(go.Bar(
            x=["Communication", "Technical Depth", "Confidence"],
            y=[
                data.get("communication", 0),
                data.get("technical_depth", 0),
                data.get("confidence", 0)
            ]
        ))
    
        st.plotly_chart(fig)
