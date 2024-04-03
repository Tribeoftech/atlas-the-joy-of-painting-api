"""
Declares SQLAlchemy ORM model for episode dates table.

Episode_Dates: ORM model for episode_dates table. Contains id, title, and episode_date columns.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Episode_Dates(Base):
	__tablename__ = 'episode_dates'
	id = Column(Integer, primary_key=True, index=True)
	title = Column(String, nullable=False)
	episode_date = Column(String, nullable=False)