from sqlalchemy import Table, Column, Integer, String, Boolean

from src.database import metadata

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("first_name", String),
    Column("last_name", String),
    Column("email", String, unique=True, index=True),
    Column("password", String),
    Column("is_active", Boolean, default=True)
)


