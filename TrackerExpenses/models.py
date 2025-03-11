from sqlachemy import create_engine, Column, Integer, String, Float, func, ForeignKey, DateTime
from sqlachemy.ext.declerative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True) #integer columns with max 256 characters cannot be empty
    name = Column(String(256), nullable=False)
    password = Column(String(256), nullable=False)
    email = Column(String(256), nullable=False)

