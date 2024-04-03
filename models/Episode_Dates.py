from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Episode_Dates(Base):
	__tablename__ = 'episode_dates'
	id = Column(Integer, primary_key=True, index=True)
	title = Column(String, nullable=False)
	episode_date = Column(String, nullable=False)