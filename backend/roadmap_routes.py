from fastapi import APIRouter, Depends
from backend.auth.dependencies import get_current_user
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter(prefix="/roadmap")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


@router.post("/generate")
def generate_roadmap(data: dict, user=Depends(get_current_user)):

    missing_skills = data["missing_skills"]
    target_role = data["target_role"]

    prompt = f"""
    A student wants to become a {target_role}.

    Missing skills:
    {missing_skills}

    Generate a 4 week learning roadmap to acquire these skills.
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return {"roadmap": response.choices[0].message.content}
    except Exception as e:
        return {"error": f"AI Generation failed: {str(e)}"}