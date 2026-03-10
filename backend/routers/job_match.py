from fastapi import APIRouter
from pydantic import BaseModel
from backend.services.job_matcher import match_jobs

router = APIRouter()

class SkillInput(BaseModel):
    skills: list

@router.post("/job/match")
def job_match(data: SkillInput):
    matches = match_jobs(data.skills)
    return {"matches": matches}
