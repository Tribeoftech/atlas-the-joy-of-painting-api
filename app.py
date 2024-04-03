""" Driver program for application """
from api.v1.episodes import models, views
from engine.db import engine, sessionmaker
from fastapi import FastAPI

# Bind engine to database with models and views
models.Base.metadata.create_all(bind=engine)
# Sessionmaker is a factory for creating new sessions
# Session is a context manager that provides thread-safe access to the database
sessionmaker = sessionmaker(bind=engine)
# Create new session
session = sessionmaker()

# Create new FastAPI instance
app = FastAPI()

# Bind routes to views as seen in api/v1/episodes/views.py
app.include_router(views.router)
