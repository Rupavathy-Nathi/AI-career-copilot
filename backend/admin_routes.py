from fastapi import APIRouter, Depends
from backend.auth.dependencies import get_current_user

router = APIRouter(prefix="/admin")

@router.get("/dashboard")
def admin_dashboard(user=Depends(get_current_user)):

    if user["role"] != "admin":
        return {"error": "Access denied"}

    return {"message": "Welcome to admin dashboard"}