from fastapi import APIRouter, Depends
from backend.auth.dependencies import get_current_user
from backend.database import users_collection, interviews_collection, resumes_collection, questions_collection
from pydantic import BaseModel
from bson import ObjectId

router = APIRouter(prefix="/admin")

class QuestionCreate(BaseModel):
    question: str

# Dependency to check admin role
def verify_admin(user: dict = Depends(get_current_user)):
    if user.get("role") != "admin":
        from fastapi import HTTPException
        raise HTTPException(status_code=403, detail="Access denied")
    return user

@router.get("/dashboard")
def admin_dashboard(admin=Depends(verify_admin)):
    return {"message": "Welcome to admin dashboard"}

@router.get("/stats")
def get_stats(admin=Depends(verify_admin)):
    users_count = users_collection.count_documents({})
    interviews_count = interviews_collection.count_documents({})
    return {"users": users_count, "interviews": interviews_count}

@router.get("/interviews")
def get_interviews(admin=Depends(verify_admin)):
    # Fetch recent interviews
    interviews = list(interviews_collection.find({}, {"_id": 0}).sort("date", -1).limit(50))
    return {"interviews": interviews}

@router.get("/resumes")
def get_resumes(admin=Depends(verify_admin)):
    # Fetch recent resumes with scores
    resumes = list(resumes_collection.find({}, {"_id": 0}).sort("date", -1).limit(50))
    return {"resumes": resumes}

@router.get("/questions")
def get_questions(admin=Depends(verify_admin)):
    questions = []
    for q in questions_collection.find():
        questions.append({"id": str(q["_id"]), "question": q["question"]})
    return {"questions": questions}

@router.post("/questions")
def add_question(data: QuestionCreate, admin=Depends(verify_admin)):
    result = questions_collection.insert_one({"question": data.question})
    return {"message": "Question added", "id": str(result.inserted_id)}

@router.delete("/questions/{q_id}")
def delete_question(q_id: str, admin=Depends(verify_admin)):
    questions_collection.delete_one({"_id": ObjectId(q_id)})
    return {"message": "Question deleted"}

@router.get("/users")
def get_users(admin=Depends(verify_admin)):
    users = []
    for u in users_collection.find():
        users.append({
            "id": str(u["_id"]),
            "name": u.get("name", "Unknown"),
            "email": u.get("email", "Unknown"),
            "role": u.get("role", "student")
        })
    return {"users": users}

@router.delete("/users/{user_id}")
def delete_user(user_id: str, admin=Depends(verify_admin)):
    result = users_collection.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count == 1:
        return {"message": "User deleted"}
    else:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="User not found")