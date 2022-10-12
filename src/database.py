import sqlalchemy
from fastapi import FastAPI
import databases

from src.config import settings

DATABASE_URL = settings.DATABASE_URL

metadata = sqlalchemy.MetaData()

database = databases.Database(DATABASE_URL)

engine = sqlalchemy.create_engine(DATABASE_URL)

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def connect():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
