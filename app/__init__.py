from flask import Flask
from sqlalchemy import create_engine
from database_setup import Base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

APPLICATION_NAME = "Catalog Application"

# Connect to Database and create database session
engine = create_engine('sqlite:///catalog_database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

from app import login
from app import views
from app import views_json
