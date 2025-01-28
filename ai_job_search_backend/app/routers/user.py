from fastapi import APIRouter, HTTPException
from app.models.user import User  # Correct the import path
from db import db

router = APIRouter()

@router.get("/users")
async def get_users():
    users_collection = db["users"]
    users = await users_collection.find().to_list(100)  # Limit to 100 users
    return {"users": users}

@router.post("/users")
async def create_user(user: User):
    users_collection = db["users"]
    new_user = user.model_dump()  # Use model_dump instead of dict()
    result = await users_collection.insert_one(new_user)
    return {"message": f"User {result.inserted_id} created successfully"}
