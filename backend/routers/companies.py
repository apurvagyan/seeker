from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas, models
from app.database import get_db

router = APIRouter(
    prefix="/companies",
    tags=["companies"],
)

@router.post("/", response_model=schemas.Company)
def create_company(company: schemas.CompanyCreate, db: Session = Depends(get_db)):
    db_company = models.Company(**company.dict())
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company

@router.get("/", response_model=List[schemas.Company])
def read_companies(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    companies = db.query(models.Company).offset(skip).limit(limit).all()
    return companies

@router.get("/{company_id}", response_model=schemas.Company)
def read_company(company_id: int, db: Session = Depends(get_db)):
    company = db.query(models.Company).filter(models.Company.id == company_id).first()
    if company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return company

@router.post("/{company_id}/jobs/", response_model=schemas.Job)
def create_job_for_company(
    company_id: int, job: schemas.JobCreate, db: Session = Depends(get_db)
):
    db_job = models.Job(**job.dict(), company_id=company_id)
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

@router.get("/{company_id}/jobs/", response_model=List[schemas.Job])
def read_jobs_for_company(company_id: int, db: Session = Depends(get_db)):
    jobs = db.query(models.Job).filter(models.Job.company_id == company_id).all()
    return jobs
