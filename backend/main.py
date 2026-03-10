from fastapi import FastAPI
from backend.auth.routes import router as auth_router
from backend.student_routes import router as student_router
from backend.admin_routes import router as admin_router
from backend.resume_routes import router as resume_router
from backend.resume_analyzer_routes import router as resume_analyzer_router
from backend.ats_routes import router as ats_router
from backend.jd_routes import router as jd_router
from backend.skill_gap_routes import router as skill_gap_router
app = FastAPI()

app.include_router(auth_router)
app.include_router(student_router)
app.include_router(admin_router)
app.include_router(resume_router)
app.include_router(resume_analyzer_router)
app.include_router(ats_router)
app.include_router(jd_router)
app.include_router(skill_gap_router)

@app.get("/")
def home():
    return {"message": "AI Career Copilot API Running"}