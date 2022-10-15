from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src import healthcheck
from src.database import database
from src.users import routes

app = FastAPI()

# routers
app.include_router(healthcheck.router)
app.include_router(routes.router)

# cors
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# database connect
@app.on_event("startup")
async def connect():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()




