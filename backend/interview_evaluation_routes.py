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

    question = data.get("question", "")
    answer = data.get("answer", "")

    prompt = f"""
    Evaluate this interview answer and give score:

    Question: {question}
    Answer: {answer}

    Return ONLY a valid JSON object with the following keys and no extra text, markdown formatting or backticks at all:
    "score" (integer 0-100),
    "communication" (integer 0-100),
    "technical_depth" (integer 0-100),
    "confidence" (integer 0-100),
    "suggestion" (string).
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        import json
        feedback = json.loads(response.choices[0].message.content.strip('` \n'))
        return feedback
    except Exception as e:
        # Fallback if AI generation or JSON parsing fails
        score = min(len(answer) // 5, 100) if isinstance(answer, str) else 50
        return {
            "score": score,
            "communication": 75,
            "technical_depth": 70,
            "confidence": 72,
            "suggestion": f"Fallback Response: Explain your approach more clearly and include examples. (Error: {str(e)})"
        }