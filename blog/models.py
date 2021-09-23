from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean

class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
