from fastapi import FastAPI

from src import healthcheck


app = FastAPI()

app.include_router(healthcheck.router)
