from fastapi import APIRouter, UploadFile, File, Form, Depends
from backend.services.speech_service import transcribe_audio
from backend.services.ai_gateway import ask_ai
from backend.auth.dependencies import get_current_user
from backend.database import interviews_collection
from datetime import datetime
import shutil
import json

router = APIRouter()

@router.post("/voice/interview")
async def voice_interview(
    audio: UploadFile = File(...),
    question: str = Form(...),
    user=Depends(get_current_user)
):

    file_path = f"temp_{audio.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(audio.file, buffer)

    try:
        import wave
        with wave.open(file_path, "rb") as wf:
            pass
        text = transcribe_audio(file_path)
        
        # Now evaluate the answer with AI
        prompt = f"""
Evaluate this interview answer and give score:

Question: {question}
Answer: {text}

Return ONLY a valid JSON object with the following keys and no extra text, markdown formatting or backticks at all:
"score" (integer 0-100),
"feedback" (string),
"ideal_answer" (string),
"suggestions" (list of strings).
"""
        reply = ask_ai(prompt)
        feedback_data = json.loads(reply.strip('` \n'))
        
        interviews_collection.insert_one({
            "student": user.get("email", "Unknown"),
            "question": question,
            "score": feedback_data.get("score", 0),
            "date": datetime.now()
        })
        
        return {
            "question": question,
            "transcribed_text": text,
            "score": feedback_data.get("score", 0),
            "feedback": feedback_data.get("feedback", "No feedback available."),
            "ideal_answer": feedback_data.get("ideal_answer", "No ideal answer available."),
            "suggestions": feedback_data.get("suggestions", [])
        }
        
    except wave.Error:
        return {"error": "Invalid audio format. Please use a valid WAV file."}
    except Exception as e:
        return {"error": f"Audio processing failed: {str(e)}"}