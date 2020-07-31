from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# URI
SQLALCHEMY_DATABASE_URI = "sqlite:///imsdb"

# engine
engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread" : False}, echo=True)

# talk to the db
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Class to describe the db
Base = declarative_base()


# dependency

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
