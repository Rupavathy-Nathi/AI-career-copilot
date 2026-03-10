from fastapi import APIRouter, Depends
from backend.auth.dependencies import get_current_user
from backend.database import resumes_collection

router = APIRouter(prefix="/ats")


@router.post("/score")
def ats_score(data: dict, user=Depends(get_current_user)):

    job_description = data["job_description"]

    resume = resumes_collection.find_one({"email": user["email"]})

    if not resume:
        return {"error": "Resume not uploaded"}

    resume_text = resume["resume_text"].lower()
    job_description = job_description.lower()

    skills = [
        "python","java","sql","fastapi",
        "docker","kubernetes","react",
        "mongodb","machine learning"
    ]

    matched = []
    missing = []

    for skill in skills:
        if skill in resume_text and skill in job_description:
            matched.append(skill)
        elif skill in job_description:
            missing.append(skill)

    score = int((len(matched) / max(len(matched)+len(missing),1)) * 100)

    return {
        "ats_score": score,
        "matched_skills": matched,
        "missing_skills": missing
    }