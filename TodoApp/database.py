from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCEHMY_DATABASE_URL = 'postgresql://postgres:Bzs37#Bzs@localhost/TodoApplicationDatabase'

engine = create_engine(SQLALCEHMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()