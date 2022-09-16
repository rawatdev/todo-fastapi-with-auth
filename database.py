from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os

# Sqlite3
# SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

# MYSQL Series
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:test1234!@127.0.0.1:3306/todoapp"

# PostgreSQL
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:3480@localhost/TodoApplicationDatabase"

# PostgreSQL Prduction
SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL")
if (SQLALCHEMY_DATABASE_URL.startswith("postgres://")):
    SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace(
        "postgres://", "postgresql://", 1)

# Sqlite3
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

# MYSQL & PostgreSQL
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
