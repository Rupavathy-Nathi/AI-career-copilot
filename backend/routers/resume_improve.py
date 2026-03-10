from fastapi import APIRouter
from pydantic import BaseModel
from backend.services.resume_improver import improve_resume

router = APIRouter()

class ResumeText(BaseModel):
    content: str

@router.post("/resume/improve")
def improve(data: ResumeText):
    improved = improve_resume(data.content)
    return {"improved_resume": improved}
