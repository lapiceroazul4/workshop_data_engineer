import json 
import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from Transformation import transformations
from sqlalchemy import func, text

#Leer config desde el JSON
with open('db_config.json', 'r') as json_file:
    data = json.load(json_file)
    usuario = data["user"]
    password = data["passwd"]
    server = data["server"]
    database = data["database"]

db_url = f"mysql+pymysql://{usuario}:{password}@{server}/{database}"
Base = declarative_base()


class Workshop(Base):

    __tablename__ = "candidates"
    Candidate_id = Column("candidate_id", Integer, primary_key=True, autoincrement=True)
    First_Name = Column("first_name", String(20))
    Last_Name = Column("last_name", String(20))
    Email = Column("email", String(50))
    Application_Date = Column("application_date", Date)
    Country = Column("country", String(20))
    YOE = Column("yoe", Integer)
    Seniority = Column("seniority", String(20))
    Technology = Column("technology", String(20))
    Code_Challenge_Score = Column("code_challenge_score", Integer)
    Technical_Interview_Score = Column("technical_interview_score", Integer)
    Is_Hired = Column("is_hired", Boolean) 

    def __init__ (self, session):
        self.session = session

    #Crear un nuevo candidato, new_candidate debe traer toda la información de dicho candidato
    def create(self, new_candidate):
        self.session.add(new_candidate)
        self.session.commit()

    #Hacer una consulta por medio del id del candidato
    #Se define como un metodo de clase puesto que no he instanciado las columnas.
    @classmethod
    def hires_by_technology(cls, session):
        query =  (
            
        session.query(cls.Technology, func.count(cls.Candidate_id).label("Number of Hires"))
        .filter(cls.Is_Hired == 1)
        .group_by(cls.Technology)
        .all()
        )

        return query
    
    @classmethod
    def hires_by_year(cls, session):
        query =  (
            
        session.query(cls.Application_Date, func.count(cls.Candidate_id).label("Number of Hires"))
        .filter(cls.Is_Hired == 1)
        .group_by(cls.Application_Date)
        .all()
        )

        return query
    
    @classmethod
    def hires_by_seniority(cls, session):
        query =  (
            
        session.query(cls.Seniority, func.count(cls.Candidate_id).label("Number of Hires"))
        .filter(cls.Is_Hired == 1)
        .group_by(cls.Seniority)
        .all()

        )
        return query
    
    @classmethod
    def hires_by_year_country(cls,session):
        list_of_countries = ["United States of America", "Colombia", "Brazil", "Ecuador"]
        query = (
            session.query(
                func.year(Workshop.Application_Date).label("Year"),
                Workshop.Country,
                func.count(Workshop.Is_Hired).label("Total_of_Hires")
            )
            .filter(Workshop.Is_Hired == 1).filter(Workshop.Country.in_(list_of_countries))
            .group_by(func.year(Workshop.Application_Date), Workshop.Country)
            .order_by("Year", text("Country"))
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

def creating_engine():
    engine = create_engine(db_url)
    return engine

#Function to create the sessions
def creating_session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

#Function to close the session
def closing_session(session):
    session.close()




