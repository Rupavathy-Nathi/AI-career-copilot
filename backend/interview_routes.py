from fastapi import APIRouter, Depends
from backend.auth.dependencies import get_current_user
from backend.services.ai_gateway import ask_ai

router = APIRouter(prefix="/interview")

@router.post("/generate")
def generate_questions(data: dict, user=Depends(get_current_user)):

    role = data["role"]
    difficulty = data["difficulty"]

    prompt = f"""
    Generate 5 interview questions for a {role}.
    Difficulty level: {difficulty}.
    """

    try:
        reply = ask_ai(prompt)
        return {"questions": reply}
    except Exception as e:
        return {"error": f"AI Generation failed: {str(e)}"}