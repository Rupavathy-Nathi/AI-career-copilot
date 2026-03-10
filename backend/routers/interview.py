from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from backend.database import db
from backend.services.ai_gateway import ask_ai
import json

router = APIRouter()

class InterviewAnswer(BaseModel):
    question: str
    answer: str

@router.post("/interview/evaluate")
def evaluate_answer(data: InterviewAnswer):
    prompt = f"""
Evaluate this interview answer and give score:

Question: {data.question}
Answer: {data.answer}

Return ONLY a valid JSON object with the following keys and no extra text, markdown formatting or backticks at all:
"score" (integer 0-100),
"communication" (integer 0-100),
"technical_depth" (integer 0-100),
"confidence" (integer 0-100),
"suggestion" (string).
"""
    try:
        reply = ask_ai(prompt)
        feedback = json.loads(reply.strip('` \n'))
    except Exception:
        # Fallback if JSON format breaks
        score = min(len(data.answer) // 5, 100)
        feedback = {
            "score": score,
            "communication": 75,
            "technical_depth": 70,
            "confidence": 72,
            "suggestion": "Explain your approach more clearly and include examples."
        }

    db.interviews_collection.insert_one({
        "user": "student",
        "score": feedback.get("score", 50),
        "date": datetime.now()
    })

    return feedback
