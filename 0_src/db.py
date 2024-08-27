import json 
import pandas as pd

from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from transformation import transformations
from sqlalchemy import func, text

# Read credentials from a JSON file
with open('db_config.json', 'r') as json_file:
    data = json.load(json_file)
    usuario = data["user"]
    password = data["passwd"]
    server = data["server"]
    database = data["database"]

db_url = f"mysql+pymysql://{usuario}:{password}@{server}/{database}"
Base = declarative_base()


class Candidate:
    """
    Candidate model for storing candidate information.
    """

    Country = Column("country", String(20))
    YOE = Column("yoe", Integer)
    Seniority = Column("seniority", String(20))
    Technology = Column("technology", String(20))
    Code_Challenge_Score = Column("code_challenge_score", Integer)
    Technical_Interview_Score = Column("technical_interview_score", Integer)
    Is_Hired = Column("is_hired", Boolean)

    def __init__(self, session):
        """
        Initialize the Candidate with a database session.
        
        :param session: SQLAlchemy session object
        """
        self.session = session

    def create(self, new_candidate):
        """
        Create a new candidate record in the database.
        
        :param new_candidate: Candidate object containing all the candidate information
        """
        self.session.add(new_candidate)
        self.session.commit()

    @classmethod
    def hires_by_technology(cls, session):
        """
        Query the number of hires by technology.
        
        :param session: SQLAlchemy session object
        :return: List of tuples containing technology and number of hires
        """
        query = (
            session.query(cls.Technology, func.count(cls.Candidate_id).label("Number of Hires"))
            .filter(cls.Is_Hired == True)
            .group_by(cls.Technology)
            .all()
        )
        return query



    def update(self, update_data):
        for key, value in update_data.items():
            setattr(self, key, value)
        self.session.commit()

    def delete(self, candidate_id):
        self.session.delete(candidate_id)
        self.session.commit()

# Creating Engine
def creating_engine():
    engine = create_engine(db_url)
    return engine

# Function to create the sessions
def creating_session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

# Function to close the session
def closing_session(session):
    session.close()




