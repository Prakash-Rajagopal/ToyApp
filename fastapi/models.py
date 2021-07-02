from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from .dbconnection import Base


class Job(Base):
    __tablename__ = 'Job'

    id = Column(Integer, primary_key=True, unique=True, index=True)
    description = Column(String)
    title = Column(String)
    location = Column(String)

    candidates = relationship("Candidate", back_populates="jobs")
    jobapp = relationship("JobApp", back_populates="appjob")


class Candidate(Base):
    __tablename__ = 'Candidate'

    email = Column(String, primary_key=True)
    name = Column(String)
    Status = Column(Boolean, default=False)
    jobid = Column(Integer, ForeignKey(Job.id))

    jobs = relationship("Job", back_populates="candidates")
    canapp = relationship("JobApp", back_populates="appcan")

class JobApp(Base):
    __tablename__ = 'JobApplication'

    appid = Column(Integer, primary_key=True)
    jid = Column(Integer, ForeignKey(Job.id))
    cid = Column(String, ForeignKey(Candidate.email))

    appjob = relationship("Job", back_populates="jobapp")
    appcan = relationship("Candidate", back_populates="canapp")