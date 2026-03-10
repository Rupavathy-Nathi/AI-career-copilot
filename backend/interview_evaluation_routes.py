from fastapi import APIRouter, Depends
from backend.auth.dependencies import get_current_user
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter(prefix="/interview")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


@router.post("/evaluate")
def evaluate_answer(data: dict, user=Depends(get_current_user)):

    question = data["question"]
    answer = data["answer"]

    prompt = f"""
    Evaluate this interview answer.

    Question: {question}
    Answer: {answer}

    Provide:
    1. Technical knowledge score (0-10)
    2. Communication score (0-10)
    3. Confidence score (0-10)
    4. Feedback for improvement
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return {"evaluation": response.choices[0].message.content}
    except Exception as e:
        return {"error": f"AI Evaluation failed: {str(e)}"}