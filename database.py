from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

# Get environment variables
user = os.getenv("POSTGRE_USER", "postgres")
password = os.getenv("POSTGRE_PWD", "")
port = os.getenv("POSTGRE_PORT", "5432")
database = os.getenv("POSTGRE_DB", "QuizeApplication")


URL_DATABASE = f"postgresql://{user}:{password}@localhost:{port}/{database}"

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
