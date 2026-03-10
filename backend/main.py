from fastapi import FastAPI
from backend.auth.routes import router as auth_router

app = FastAPI()

app.include_router(auth_router)

@app.get("/")
def home():
    return {"message": "AI Career Copilot API Running"}