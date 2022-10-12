import sqlalchemy
import databases

from src.config import settings

DATABASE_URL = settings.DATABASE_URL

metadata = sqlalchemy.MetaData()

database = databases.Database(DATABASE_URL)

engine = sqlalchemy.create_engine(DATABASE_URL)

metadata.create_all(engine)




