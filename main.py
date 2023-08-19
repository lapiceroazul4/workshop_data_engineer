from Database import Workshop, creating_engine, creating_session, closing_session
from Transformation import transformations
import pandas as pd

#Creating engine
engine1 = creating_engine()

#Creating session
session1 = creating_session(engine1)

objecto2 = transformations("candidates.csv")
objecto2.normalizing()
objecto2.importing_db(engine1)

#Now my table is created in the DB, now is time to make querys
consulta = Workshop(session1)

#Hires by Technology
hires_by_technology = consulta.hires_by_technology(session1)

for r in hires_by_technology:
    print(r)

hires_technology = pd.DataFrame(hires_by_technology)
hires_technology.to_csv("hires_technology", index=False)

#Hires by Seniority
hires_by_seniority = consulta.hires_by_seniority(session1)

for r in hires_by_seniority:
    print(r)

hires_seniority = pd.DataFrame(hires_by_seniority)
hires_seniority.to_csv("hires_seniority", index=False)   

#Hires by Year
hires_by_year = consulta.hires_by_year(session1)

for r in hires_by_year:
    print(r)

hires_year = pd.DataFrame(hires_by_year)
hires_year.to_csv("hires_year", index=False)   

#Hires by Years and Countries
hires_by_year_country = consulta.hires_by_year_country(session1)

for r in hires_by_year_country:
    print(r)

hires_year_country = pd.DataFrame(hires_by_year_country)
hires_year_country.to_csv("hires_year_and_country", index=False)   


#Close connection
closing_session(session1)