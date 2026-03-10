from fastapi import APIRouter, Depends
from backend.auth.dependencies import get_current_user
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter(prefix="/coding")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


@router.post("/generate")
def generate_question(data: dict, user=Depends(get_current_user)):

    topic = data["topic"]
    difficulty = data["difficulty"]

    prompt = f"""
    Generate a coding interview problem.

    Topic: {topic}
    Difficulty: {difficulty}

    Provide:
    1. Problem statement
    2. Example input/output
    3. Explanation
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return {"problem": response.choices[0].message.content}
    except Exception as e:
        return {"error": f"AI Generation failed: {str(e)}"}