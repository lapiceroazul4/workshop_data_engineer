import pandas as pd

class Transformations:
    """
    A class to perform data transformations on a CSV file.
    """

    def __init__(self, archivo):
        """
        Initialize the Transformations class with a CSV file.
        
        :param archivo: Path to the CSV file
        """
        # Read the CSV file with pandas
        self.df = pd.read_csv(archivo, sep=";")

    def normalizing(self):
        """
        Normalize the DataFrame by renaming columns and adding the 'is_hired' column.
        """
        # Rename columns to match the database schema
        new_columns = {
            "First Name": "first_name",
            "Last Name": "last_name",
            "Email": "email",
            "Application Date": "application_date",
            "Country": "country",
            "YOE": "yoe",
            "Seniority": "seniority",
            "Technology": "technology",
            "Code Challenge Score": "code_challenge_score",
            "Technical Interview Score": "technical_interview_score"
        }
        self.df.rename(columns=new_columns, inplace=True)
        
        # The CSV does not have the 'is_hired' column, so we create it using pandas
        self.df["is_hired"] = self.df.apply(
            lambda row: 1 if row["code_challenge_score"] >= 7 and row["technical_interview_score"] >= 7 else 0, axis=1
        )

    def importing_db(self, engine):
        """
        Import the DataFrame into the database.
        
        :param engine: SQLAlchemy engine object
        """
        self.df.to_sql("candidates", con=engine, if_exists="replace", index_label="candidate_id")
        print("Successfully Created")