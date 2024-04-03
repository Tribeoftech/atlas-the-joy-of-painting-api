""" Entire API - needs refactoring """
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Optional

app = FastAPI()
SQLALCHEMY_DATEBASE_URI = 'sqlite:///bob_ross.db'

engine = create_engine(SQLALCHEMY_DATEBASE_URI)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Episode(Base):
    __tablename__ = 'episodes'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), nullable=False, unique=True)
    date = Column(String(20), nullable=False, unique=True)

    def __repr__(self):
        return f'<Episode {self.title}>'

# Object structure for post requests
class Add_Episode(BaseModel):
    """ Episode Model """
    title: str
    date: str

# Object structure for put requests
class Update_Episode(BaseModel):
    """ Episode Model """
    title: Optional[str] = None
    date: Optional[str] = None

# Database setup
Base.metadata.create_all(bind=engine)
session = sessionmaker(bind=engine)
s = session()

@app.get("/api/v1/episodes")
def all_episodes():
    """ Define GET request made to /episodes endpoint """
    eps = s.query(Episode).all()
    return eps

# # How to handle query parameters
# @app.get("/api/v1/episodes")
# def search_episodes(subject: Optional[int] = None, color: Optional[int] = None, date: Optional[int] = None):
#     ep = s.query(Episode).filter_by(subject=subject, color=color, date=date).first()
#     if not ep:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
#     return ep

@app.get("/api/v1/episodes/{ep_id}")
def one_episode(ep_id: int):
    """ Define GET request made to endpoint including ep_id """
    ep = s.query(Episode).filter_by(id=ep_id).first()
    if not ep:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return ep

@app.post("/api/v1/episodes/{ep_id}")
def add_episode(ep_id: int, ep: Add_Episode):
    """ Define POST request made to endpoint including ep_id """
    new_ep = Episode(id=ep_id, title=ep.title, date=ep.date)
    s.add(new_ep)
    s.commit()
    return new_ep

@app.put("/api/v1/episodes/{ep_id}")
def update_episode(ep_id: int, ep: Update_Episode):
    """ Define PUT request made to endpoint including ep_id """
    episode = s.query(Episode).filter_by(id=ep_id).first()
    if not episode:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    if ep.title:
        episode.title = ep.title
    if ep.date:
        episode.date = ep.date
    s.commit()
    return episode

# Run with: uvicorn fast_api:app --reload
