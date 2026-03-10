import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
def analyze_resume(resume_text):

    resume_text = resume_text[:6000]

    prompt = f"""
    Analyze this resume and provide:

    1. Resume Score (0-100)
    2. Detected Skills
    3. Missing Skills
    4. Suggestions to improve the resume

    Resume:
    {resume_text}
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"AI Analysis failed: {str(e)}"