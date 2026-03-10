from fastapi import FastAPI
from backend.auth.routes import router as auth_router
from backend.student_routes import router as student_router
from backend.admin_routes import router as admin_router
from backend.resume_routes import router as resume_router
from backend.resume_analyzer_routes import router as resume_analyzer_router
from backend.ats_routes import router as ats_router
from backend.jd_routes import router as jd_router
from backend.skill_gap_routes import router as skill_gap_router
from backend.roadmap_routes import router as roadmap_router
from backend.interview_routes import router as interview_router
from backend.interview_evaluation_routes import router as interview_eval_router
from backend.coding_routes import router as coding_router
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from backend.utils.logger import get_logger
from backend.routers import voice_interview
app = FastAPI()
logger = get_logger()

app.include_router(auth_router)
app.include_router(student_router)
app.include_router(admin_router)
app.include_router(resume_router)
app.include_router(resume_analyzer_router)
app.include_router(ats_router)
app.include_router(jd_router)
app.include_router(skill_gap_router)
app.include_router(roadmap_router)
app.include_router(interview_router)
app.include_router(interview_eval_router)
app.include_router(coding_router)
app.include_router(voice_interview.router)
logger = get_logger()

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error: {exc}")
    return JSONResponse(
        status_code=500,
        content={"message": "Internal server error"}
    )

@app.get("/")
def home():
    return {"message": "AI Career Copilot API Running"}