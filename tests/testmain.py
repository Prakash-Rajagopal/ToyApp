from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from myfirstpython.fastapi.dbconnection import Base
from myfirstpython.fastapi.main import app, get_db
#from myfirstpython.models import Job

SQLALCHEMY_DATABASE_URL = "sqlite:///C:\\Users\\HP\\test.db"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db()] = override_get_db()

client = TestClient(app)


def test_create_job():
    response = client.post("/jobs/", json={"description": "Manage Product Development",
                                           "title": "Product Manager",
                                           "location": "Bangalore"},
                           )
    assert response.status_code == 200, response.text
    data = response.json()
    #assert data: "title"  == "Product Manager"
    #assert id in data
    #Job.id = data[id]
