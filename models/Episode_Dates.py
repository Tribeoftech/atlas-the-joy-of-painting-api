"""
Declares SQLAlchemy ORM model for episode dates table.

Contains:
- Episode_Dates: SQLAlchemy ORM model class for episode_dates table.
  Has id, title, and episode_date columns.
"""
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Episode_Dates(Base):
    __tablename__ = 'episode_dates'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    episode_date = Column(String, nullable=False)

    @classmethod
    def process_data(cls):
        with open('datasets/The_Joy_Of_Painting-Episode_Dates.txt', 'r') as f:
            with open('datasets/Episode_Dates.txt', 'w') as f2:
                for line in f:
                    f2.write(line.replace('(', '').replace(')', ''))

        df = pd.read_csv('datasets/Episode_Dates.txt', header=None, sep='\t', names=['title', 'episode_date'])

        engine = create_engine('postgresql://postgres:hank@localhost:5432/postgres')

        df.to_sql('episode_dates', engine, if_exists='replace')

