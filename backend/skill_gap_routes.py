from fastapi import APIRouter, Depends
from backend.auth.dependencies import get_current_user
from backend.database import resumes_collection

router = APIRouter(prefix="/skill-gap")

@router.post("/analyze")
def skill_gap(data: dict, user=Depends(get_current_user)):

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

    total = len(matched) + len(missing)

    gap_score = int((len(matched) / total) * 100) if total > 0 else 0

    return {
        "matched_skills": matched,
        "missing_skills": missing,
        "gap_score": gap_score
    }