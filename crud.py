from sqlalchemy.orm import Session

from . import models, schemas


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
