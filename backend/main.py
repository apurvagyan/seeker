from fastapi import FastAPI
from app.routers import companies
from app.database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(companies.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to CareerNavigator API"}
