from pymongo import MongoClient

MONGO_URL = "mongodb+srv://career_admin:strongpassword123@cluster0.4xf5le3.mongodb.net/?appName=Cluster0"

client = MongoClient(MONGO_URL)

db = client["career_copilot_db"]

users_collection = db["users"]
resumes_collection = db["resumes"]
interviews_collection = db["interviews"]
coding_collection = db["coding_practice"]
jobs_collection = db["job_descriptions"]
roadmaps_collection = db["career_roadmaps"]