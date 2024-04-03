""" Create new database and bind engine to it """
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Sqlite database does not connect with sensitive info so find here
# But recommended to use .env file or similar
SQLALCHEMY_DATEBASE_URI = 'sqlite:///happy_lil_trees.db'

# Create engine
# Create engine bound to SQLite database
engine = create_engine(SQLALCHEMY_DATEBASE_URI)
# Create new sessionmaker
# Sessionmaker is a factory for creating new sessions
# SessionLocal is a thread-local scoped session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base will be used to create new tables
Base = declarative_base()
