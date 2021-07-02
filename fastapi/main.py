from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from myfirstpython.fastapi import models, crud, schemas
from myfirstpython.fastapi.dbconnection import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/jobs/", response_model=schemas.JobCreate)
def create_job(job: schemas.JobCreate, db: Session = Depends(get_db)):
    db_job = crud.get_job(db, job.title)
    if db_job:
        raise HTTPException(status_code=400, detail="Job already Posted")
        return crud.create_job(db=db, job=job)


@app.get("/jobs/", response_model=List[schemas.Job])
def read_jobs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    jobs = crud.get_jobs(db, skip=skip, limit=limit)
    return jobs


@app.get("/jobs/{job_id}", response_model=schemas.Job)
def read_job(job_id: int, db: Session = Depends(get_db)):
    db_job = crud.get_job(db, job_id=job_id)
    if db_job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return db_job


@app.post("/cands/", response_model=schemas.CanCreate)
def create_can(can: schemas.CanCreate, db: Session = Depends(get_db)):
    db_can = crud.get_candidate(db, can.email)
    if db_can:
        raise HTTPException(status_code=400, detail="Candidate already Present")
        return crud.create_candidate(db=db, can=can)


@app.get("/cands/", response_model=List[schemas.Can])
def read_cans(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cans = crud.get_candidates(db, skip=skip, limit=limit)
    return cans


@app.get("/cands/{email}", response_model=schemas.Can)
def read_can(email: str, db: Session = Depends(get_db)):
    db_can = crud.get_candidate(db, email)
    if db_can is None:
        raise HTTPException(status_code=404, detail="Candidate not found")
    return db_can


@app.get("/jobapps/", response_model=List[schemas.AppBase])
def read_jobapps(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    jobapps = crud.get_jobapps(db, skip=skip, limit=limit)
    return jobapps


@app.get("/jobapps/{appid}", response_model=schemas.AppBase)
def read_jobapp(appid: int, db: Session = Depends(get_db)):
    db_jobapp = crud.get_jobapp(db, appid)
    if db_jobapp is None:
        raise HTTPException(status_code=404, detail="Job Application not found")
    return db_jobapp
