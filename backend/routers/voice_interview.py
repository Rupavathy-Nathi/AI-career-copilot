from fastapi import APIRouter, UploadFile, File
from backend.services.speech_service import transcribe_audio
import shutil

router = APIRouter()

@router.post("/voice/interview")

async def voice_interview(audio: UploadFile = File(...)):

    file_path = f"temp_{audio.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(audio.file, buffer)

    text = transcribe_audio(file_path)

    return {
        "transcribed_text": text
    }