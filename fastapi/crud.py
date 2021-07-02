from sqlalchemy.orm import Session

from myfirstpython.fastapi import models, schemas


def get_job(db: Session, job_id: int):
    return db.query(models.Job).filter(models.Job.id == job_id).first()


def get_jobs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Job).offset(skip).limit(limit).all()


def create_job(db: Session, job: schemas.JobCreate):
    db_job = models.Job(description=job.description, title=job.title, location=job.location)
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job


def get_candidate(db: Session, email: str):
    return db.query(models.Candidate).filter(models.Candidate.email == email).first()


def get_candidates(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Candidate).offset(skip).limit(limit).all()


def create_candidate(db: Session, candidate: schemas.CanCreate):
    db_candidate = models.Candidate(email=candidate.email, name=candidate.name)
    db.add(db_candidate)
    db.commit()
    db.refresh(db_candidate)
    return db_candidate


def get_jobapp(db: Session, appid: int):
    return db.query(models.JobApp).filter(models.JobApp.appid) == appid.first()


def get_jobapps(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.JobApp).offset(skip).limit(limit).all()
