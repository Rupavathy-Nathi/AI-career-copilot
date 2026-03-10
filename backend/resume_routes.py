from fastapi import APIRouter, UploadFile, File, Depends
from backend.auth.dependencies import get_current_user
from backend.database import resumes_collection
import PyPDF2

router = APIRouter(prefix="/resume")

@router.post("/upload")
def upload_resume(file: UploadFile = File(...), user=Depends(get_current_user)):

    pdf_reader = PyPDF2.PdfReader(file.file)

    text = ""

    for page in pdf_reader.pages:
        text += page.extract_text()

    resume_data = {
        "email": user["email"],
        "resume_text": text
    }

    resumes_collection.insert_one(resume_data)

    return {"message": "Resume uploaded successfully"}