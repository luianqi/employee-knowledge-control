from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    DATABASE_URL: str
    REDIS_HOST: str
    REDIS_POST: int
    REDIS_DB: int
    SECRET_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()
