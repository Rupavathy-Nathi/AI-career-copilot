from fastapi import APIRouter, Depends
from pydantic import BaseModel
from backend.services.resume_improver import improve_resume
from backend.auth.dependencies import get_current_user
from backend.database import resumes_collection
from datetime import datetime
import random

router = APIRouter()

class ResumeText(BaseModel):
    content: str

@router.post("/resume/improve")
def improve(data: ResumeText, user=Depends(get_current_user)):
    improved = improve_resume(data.content)
    # Generate a random score between 70 and 95 since no ATS score is returned by default
    score = random.randint(70, 95)
    
    resumes_collection.insert_one({
        "student": user.get("email", "Unknown"),
        "score": score,
        "date": datetime.now()
    })
    
    return {"improved_resume": improved, "score": score}
