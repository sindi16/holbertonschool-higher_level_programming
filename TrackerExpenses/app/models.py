from sqlalchemy import create_engine, Column, Integer, String, Float, func, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, autoincrement=True) #integer columns with max 256 characters cannot be empty
    name = Column(String(256), nullable=False)
    password = Column(String(256), nullable=False)
    email = Column(String(256), nullable=False)

    #create a relationship between the user and the expenses
    #create a relationship between the user and the budgets
    expenses = relationship("Expense", back_populates="user")
    budgets = relationship("Budget", back_populates="user")


class Category(Base):
    __tablename__ ="Categories"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(256), nullable=False)

    expenses = relationship("Expense", back_populates="category")
    budget = relationship("Budget", back_pupulates="category")
    #defines a one to many relationship between the category and the expenses
class Expense(Base):
    __tablename__ = "Expenses"
    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Float, nullable=False)
    expense_date= Column(DateTime, nullable=False, default=func.current_timestamp())
    description = Column(String(256), nullable=False)
    user_id = Column(Integer, ForeignKey("Users.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("Categories.id")) #its a foreign key referencing the category table Categoeries.ID

    #create a relationship between user and expenses
    #create a relationship between category and expenses
    category=relationship("Category", back_populates="expenses")
    user=relationship("User", back_populates="expenses")

class Budget(Base):
    __tablename__ = "Budgets"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    amount = Column(Float, nullable=False)
    user_id =Column(Integer, ForeignKey("Users.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("Category.id"), nullable=False)
    #create a relationship between user and budgets
    user = relationship("User", back_populates="budgets")
    category = relationship("Category", back_populates="budgets")


    #connecting with databse
DATABASE_URL = "mysql+pymysql://root:root@localhost/TrackerExpenses"
engine = create_engine(DATABASE_URL) #Establishes the connection.
Base.metadata.create_all(engine)    #creates the tables if they dont already exists

Session = sessionmaker(bind=engine) #creates a session maker object that configures the session
session = Session() #creates a session object to interact with the database


session.close()