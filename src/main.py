import os

from dotenv import load_dotenv
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi import FastAPI

from src import healthcheck

load_dotenv(".env")

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"].replace("postgres://", "postgresql://", 1))

app.include_router(healthcheck.router)
