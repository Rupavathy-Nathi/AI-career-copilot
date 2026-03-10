from fastapi import APIRouter, Depends
from groq import Groq
import os
from dotenv import load_dotenv
from backend.auth.dependencies import get_current_user

from backend.models.jd_model import JDRequest
from backend.utils.logger import get_logger

load_dotenv()

router = APIRouter(prefix="/job")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
logger = get_logger()

@router.post("/analyze")
def analyze_jd(data: JDRequest, user=Depends(get_current_user)):
    logger.info("JD analysis request received")

    job_description = data.job_description

    prompt = f"""
    Analyze this job description and return:

    1. Role
    2. Required Skills
    3. Responsibilities
    4. Difficulty (Easy/Medium/Hard)

    Job Description:
    {job_description}
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        logger.success("JD analyzed successfully")
        return {"analysis": response.choices[0].message.content}
    except Exception as e:
        logger.error(f"JD analysis failed: {e}")
        return {"error": "JD analysis failed"}