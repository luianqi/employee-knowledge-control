from sqlalchemy import Column, Integer, String, Boolean, Enum

from src.database import Base
from src.users.schemas import Roles


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(Enum(Roles), default="user")
    is_active = Column(Boolean, default=True)












