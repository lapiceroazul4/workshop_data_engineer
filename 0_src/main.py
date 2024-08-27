import pandas as pd

from db import Workshop, creating_engine, creating_session, closing_session
from transformation import transformations

def main():
    """
    Main function to perform data transformations and queries on the database.
    """
    # Create engine
    engine = creating_engine()

    # Create session
    session = creating_session(engine)

    # Perform data transformations
    transformer = Transformations("candidates.csv")
    transformer.normalizing()
    transformer.importing_db(engine)

    # Create Workshop object for querying
    workshop = Workshop(session)

    # Query hires by technology and save to CSV
    hires_by_technology = workshop.hires_by_technology(session)
    for record in hires_by_technology:
        print(record)
    hires_technology_df = pd.DataFrame(hires_by_technology)
    hires_technology_df.to_csv("hires_technology.csv", index=False)

    # Query hires by seniority and save to CSV
    hires_by_seniority = workshop.hires_by_seniority(session)
    for record in hires_by_seniority:
        print(record)
    hires_seniority_df = pd.DataFrame(hires_by_seniority)
    hires_seniority_df.to_csv("hires_seniority.csv", index=False)

    # Query hires by year and save to CSV
    hires_by_year = workshop.hires_by_year(session)
    for record in hires_by_year:
        print(record)
    hires_year_df = pd.DataFrame(hires_by_year)
    hires_year_df.to_csv("hires_year.csv", index=False)

    # Query hires by year and country and save to CSV
    hires_by_year_country = workshop.hires_by_year_country(session)
    for record in hires_by_year_country:
        print(record)
    hires_year_country_df = pd.DataFrame(hires_by_year_country)
    hires_year_country_df.to_csv("hires_year_and_country.csv", index=False)

    # Close session
    closing_session(session)

if __name__ == "__main__":
    main()