from fastapi import FastAPI
#from ai_job_search_backend.db import get_database  # Import the MongoDB connection from db.py
from db import get_database
from app.routers.user import router as user_router  # Import user router from the app.routers package
from app.routers.job import router as job_router

app = FastAPI()

app.include_router(user_router)
app.include_router(job_router, prefix="/api", tags=["Jobs"])

# Example route to check the connection
@app.get("/")
async def root():
    db = get_database()  # Get the database client from db.py
    return {"message": "Connected to MongoDB successfully!"}

# Example route to fetch all users
@app.get("/users")
async def get_users():
    db = get_database()
    users_collection = db["users"]  # Specify the collection you want to use
    users = list(users_collection.find())  # Get all documents in the collection
    return {"users": users}
