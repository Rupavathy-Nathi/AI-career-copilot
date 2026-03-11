from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI") or os.getenv("MONGO_URL")

client = MongoClient(MONGO_URI)

db = client["career_copilot_db"]

users_collection = db["users"]
resumes_collection = db["resumes"]
interviews_collection = db["interviews"]
coding_collection = db["coding_practice"]
jobs_collection = db["job_descriptions"]
roadmaps_collection = db["career_roadmaps"]