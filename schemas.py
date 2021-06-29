from typing import List, Optional
from pydantic import BaseModel


class JobBase(BaseModel):
    description: str
    title: str


class JobCreate(JobBase):
    location: str


class Job(JobBase):
    id: int

    class Config:
        orm_mode = True

