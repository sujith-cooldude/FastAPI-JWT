from sqlalchemy import Column, Integer, String
from database import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, index=True, primary_key=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)