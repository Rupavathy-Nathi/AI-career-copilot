from fastapi import FastAPI
from backend.auth.routes import router as auth_router
from backend.student_routes import router as student_router
from backend.admin_routes import router as admin_router
from backend.resume_routes import router as resume_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(student_router)
app.include_router(admin_router)
app.include_router(resume_router)

@app.get("/")
def home():
    return {"message": "AI Career Copilot API Running"}