import redis

from src.config import settings


def create_redis():
    return redis.ConnectionPool(
        host=settings.REDIS_HOST,
        port=settings.REDIS_POST,
        db=settings.REDIS_DB,
        decode_responses=True
    )


pool = create_redis()


# redis connection
def get_redis():
    return redis.Redis(connection_pool=pool)
