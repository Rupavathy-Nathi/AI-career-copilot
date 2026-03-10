from fastapi import APIRouter, Depends
from backend.database import resumes_collection
from backend.auth.dependencies import get_current_user
from backend.ai_services import analyze_resume

router = APIRouter(prefix="/resume")


@router.get("/analyze")
def analyze(user=Depends(get_current_user)):

    resume = resumes_collection.find_one({"email": user["email"]})

    if not resume:
        return {"error": "Resume not uploaded"}

    result = analyze_resume(resume["resume_text"])

    return {"analysis": result}