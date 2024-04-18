from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    # check_same_thread Allows multiple threads to use the same connection, for
    # when multiple request-handling threads might access the database at the same time
    # SQLite has threading issues, defaults to false
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# Flush -> Sync session state with database 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()