import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

# MongoDB connection setup
MONGO_URI = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_URI)
db = client["job_platform"]

async def seed_jobs():
    jobs_collection = db["jobs"]
    
    # Example job postings
    sample_jobs = [
        {
            "title": "Software Engineer",
            "company": "TechCorp Inc.",
            "description": "Develop and maintain software applications.",
            "location": "New York, NY",
            "salary": 120000,
            "skills": ["Python", "FastAPI", "MongoDB"],
            "posted_date": "2025-01-27"
        },
        {
            "title": "Data Scientist",
            "company": "Data Solutions Ltd.",
            "description": "Analyze and interpret complex data to help businesses make decisions.",
            "location": "San Francisco, CA",
            "salary": 150000,
            "skills": ["Python", "Machine Learning", "Data Analysis"],
            "posted_date": "2025-01-20"
        },
        {
            "title": "Frontend Developer",
            "company": "Creative Coders",
            "description": "Design and implement user interfaces for web applications.",
            "location": "Remote",
            "salary": 90000,
            "skills": ["JavaScript", "React.js", "CSS"],
            "posted_date": "2025-01-15"
        }
    ]
    
    # Insert sample data into the jobs collection
    await jobs_collection.insert_many(sample_jobs)
    print("Sample job data inserted successfully!")

# Run the seeding script
if __name__ == "__main__":
    asyncio.run(seed_jobs())
