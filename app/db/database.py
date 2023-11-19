from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from getpass import getpass

from app.core.config import settings

"""
database url is dialect+driver://username:password@db_address/db_name
To connect to mysql/mariadb, pymysql module is required to install.
The purpose of using SqlAlchemy is to abstract sql syntax from the programmer/scripter,
hence there should be no sql syntax used, to use sql syntax use the execute method of the create_engine object.
"""

# join the inputs into a complete database url.
url = f"postgresql://{settings.DB_USER}:{settings.DB_PASS}@{settings.DB_IP}/{settings.DB_NAME}"
# url = f"postgresql://{db_user}:{db_pass}@0.0.0.0:5432/{db_name}"

# Create an engine object.
engine = create_engine(url, echo=True)

# Create database if it does not exist.
if not database_exists(engine.url):
    create_database(engine.url)

# Connect the database if exists.
engine.connect()

# Each instance of the SessionLocal class will be a database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# we will inherit from this class to create each of the database models or classes (the ORM models):
Base = declarative_base()
