from fastapi import APIRouter, Depends
from backend.auth.dependencies import get_current_user
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter(prefix="/interview")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


@router.post("/generate")
def generate_questions(data: dict, user=Depends(get_current_user)):

    role = data["role"]
    difficulty = data["difficulty"]

    prompt = f"""
    Generate 5 interview questions for a {role}.
    Difficulty level: {difficulty}.
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return {"questions": response.choices[0].message.content}
    except Exception as e:
        return {"error": f"AI Generation failed: {str(e)}"}