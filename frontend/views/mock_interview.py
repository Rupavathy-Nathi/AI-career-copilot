import streamlit as st
import requests
import plotly.graph_objects as go

def show():
    
    st.title("Mock Interview")
    
    question = st.text_area("Interview Question")
    
    answer = st.text_area("Your Answer")
    
    if st.button("Evaluate Answer"):
    
        response = requests.post(
            "http://localhost:8000/interview/evaluate",
            json={
                "question": question,
                "answer": answer
            }
        )
    
        data = response.json()
    
        st.success(f"Overall Score: {data['score']}/100")
    
        col1, col2, col3 = st.columns(3)
    
        col1.metric("Communication", data["communication"])
        col2.metric("Technical Depth", data["technical_depth"])
        col3.metric("Confidence", data["confidence"])
    
        st.subheader("AI Suggestion")
    
        st.info(data["suggestion"])
    
        fig = go.Figure()
    
        fig.add_trace(go.Bar(
            x=["Communication", "Technical Depth", "Confidence"],
            y=[
                data["communication"],
                data["technical_depth"],
                data["confidence"]
            ]
        ))
    
        st.plotly_chart(fig)
