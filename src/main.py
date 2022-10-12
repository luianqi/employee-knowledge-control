from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src import healthcheck

app = FastAPI()

app.include_router(healthcheck.router)

# cors
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


