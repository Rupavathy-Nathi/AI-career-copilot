from fastapi import APIRouter
from backend.database import db

router = APIRouter()

@router.get("/interview/stats")
def stats():
    # Only return _id as string or remove it since it's an ObjectId that isn't JSON serializable automatically in basic usage
    data = list(db.interviews_collection.find({}, {"_id": 0}))
    return {"history": data}
