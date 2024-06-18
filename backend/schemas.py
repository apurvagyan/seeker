from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class JobBase(BaseModel):
    title: str
    description: Optional[str] = None
    start_date: date
    end_date: date

class JobCreate(JobBase):
    company_id: int

class Job(JobBase):
    id: int

    class Config:
        orm_mode = True

class CompanyBase(BaseModel):
    name: str
    description: Optional[str] = None

class CompanyCreate(CompanyBase):
    pass

class Company(CompanyBase):
    id: int
    jobs: List[Job] = []

    class Config:
        orm_mode = True
