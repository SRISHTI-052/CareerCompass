from pydantic import BaseModel, Field
from typing import Optional, List

class Job(BaseModel):
    title: str = Field(..., description="The title of the job position")
    company: str = Field(..., description="The name of the company offering the job")
    description: str = Field(..., description="A detailed description of the job")
    location: str = Field(..., description="The location of the job")
    salary: Optional[float] = Field(None, description="The salary offered for the job")
    skills: List[str] = Field(..., description="A list of required skills for the job")
    posted_date: Optional[str] = Field(None, description="The date the job was posted")

    class Config:
        schema_extra = {
            "example": {
                "title": "Software Engineer",
                "company": "TechCorp Inc.",
                "description": "Develop and maintain software applications.",
                "location": "New York, NY",
                "salary": 120000,
                "skills": ["Python", "FastAPI", "MongoDB"],
                "posted_date": "2025-01-27"
            }
        }
