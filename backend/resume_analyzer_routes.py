from fastapi import APIRouter, Depends
from backend.database import resumes_collection
from backend.auth.dependencies import get_current_user
from backend.ai_services import analyze_resume

from backend.utils.logger import get_logger

router = APIRouter(prefix="/resume")
logger = get_logger()

@router.get("/analyze")
def analyze(user=Depends(get_current_user)):
    logger.info("Resume analysis started")

    try:
        resume = resumes_collection.find_one({"email": user["email"]})

        if not resume:
            return {"error": "Resume not uploaded"}

        result = analyze_resume(resume["resume_text"])
        logger.success("Resume analyzed successfully")
        return {"analysis": result}
    except Exception as e:
        logger.error(f"Resume analysis failed: {e}")
        return {"error": "Resume analysis failed"}