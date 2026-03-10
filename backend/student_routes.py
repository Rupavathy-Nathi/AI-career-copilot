from fastapi import APIRouter, Depends
from backend.auth.dependencies import get_current_user

router = APIRouter(prefix="/student")

@router.get("/dashboard")
def student_dashboard(user=Depends(get_current_user)):

    if user["role"] != "student":
        return {"error": "Access denied"}

    return {"message": "Welcome to student dashboard"}