from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI
import os

# Initialize the FastAPI app
app = FastAPI()

# MongoDB connection string for local development
MONGO_URI = "mongodb://localhost:27017"  # Local MongoDB URI

# MongoDB client and database initialization
client = AsyncIOMotorClient(MONGO_URI)
db = client.job_platform  # The database you're working with

# Test connection endpoint
@app.get("/")
async def test_db_connection():
    try:
        # Test MongoDB connection by accessing a collection
        await db.users.find_one()  # Try fetching a document from the 'users' collection
        return {"message": "MongoDB connected successfully!"}
    except Exception as e:
        return {"error": str(e)}
    
def get_database():
    return db

