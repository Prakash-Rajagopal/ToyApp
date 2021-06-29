from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .dbconnection import Base


class Job(Base):
    __tablename__ = 'Job'

    id = Column(Integer, primary_key=True, unique=True, index=True)
    description = Column(String)
    title = Column(String)
    location = Column(String)
