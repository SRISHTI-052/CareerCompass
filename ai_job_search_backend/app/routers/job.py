from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from bson import ObjectId
from db import db

router = APIRouter()

@router.get("/jobs", summary="Get all jobs")
async def get_all_jobs(
    location: Optional[str] = None, 
    skill: Optional[str] = None,
    limit: int = Query(10, description="Number of jobs to return")
):
    """
    Fetch all jobs or filter by location/skill.
    """
    jobs_collection = db["jobs"]
    query = {}
    if location:
        query["location"] = {"$regex": location, "$options": "i"}  # Case-insensitive match
    if skill:
        query["skills"] = {"$regex": skill, "$options": "i"}  # Case-insensitive match

    jobs = await jobs_collection.find(query).to_list(limit)
    return {"jobs": jobs}

@router.get("/jobs/{job_id}", summary="Get job by ID")
async def get_job_by_id(job_id: str):
    """
    Fetch a job by its ID.
    """
    jobs_collection = db["jobs"]
    if not ObjectId.is_valid(job_id):
        raise HTTPException(status_code=400, detail="Invalid job ID")

    job = await jobs_collection.find_one({"_id": ObjectId(job_id)})
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    return {"job": job}

@router.post("/jobs", summary="Create a new job")
async def create_job(job: dict):
    """
    Create a new job posting.
    """
    jobs_collection = db["jobs"]
    result = await jobs_collection.insert_one(job)
    return {"message": "Job created successfully", "job_id": str(result.inserted_id)}
