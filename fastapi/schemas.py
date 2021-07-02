from typing import List

from pydantic import BaseModel

#from myfirstpython.models import Candidate



class CanBase(BaseModel):
    email: str


class CanCreate(CanBase):
    name: str


class Can(CanBase):
    jobid: int
    status: bool
#    jobs: List[Job] = []

    class Config:
        orm_mode = True


class JobBase(BaseModel):
    description: str
    title: str


class JobCreate(JobBase):
    location: str


class Job(JobBase):
    id: int
    candidates: List[Can] = []

    class Config:
        orm_mode = True


class AppBase(BaseModel):
    appid: int
    jid: int
    cid: str
    is_applied: bool
    appjob: List[Job] = []
    appcan: List[Can] = []

    class Config:
        orm_mode = True