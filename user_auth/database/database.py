from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("DATBASRURL")
engine = create_engine(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
