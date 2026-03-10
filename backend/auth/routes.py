from fastapi import APIRouter
from backend.database import users_collection
from backend.auth.auth_utils import hash_password, verify_password, create_access_token

router = APIRouter()


@router.post("/register")
def register(user: dict):

    user["password"] = hash_password(user["password"])

    users_collection.insert_one(user)

    return {"message": "User registered successfully"}


@router.post("/login")
def login(data: dict):

    user = users_collection.find_one({"email": data["email"]})

    if not user:
        return {"error": "User not found"}

    if not verify_password(data["password"], user["password"]):
        return {"error": "Invalid password"}

    token = create_access_token({
        "email": user["email"],
        "role": user.get("role", "student")
    })

    return {
        "access_token": token,
        "email": user["email"],
        "role": user.get("role", "student"),
        "message": "Login successful"
    }