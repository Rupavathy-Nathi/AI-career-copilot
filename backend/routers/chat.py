from fastapi import APIRouter
from pydantic import BaseModel
from backend.services.ai_gateway import ask_ai

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
def chat(data: ChatRequest):
    try:
        reply = ask_ai(data.message)
        return {"reply": reply}
    except Exception as e:
        return {"error": f"AI Chat failed: {str(e)}"}
