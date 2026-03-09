from fastapi import FastAPI
from backend.database import users_collection

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Career Copilot API Running"}

@app.get("/test-db")
def test_db():
    count = users_collection.count_documents({})
    return {"users_in_db": count}