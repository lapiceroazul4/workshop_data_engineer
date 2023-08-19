import pandas as pd

class transformations():

    def __init__(self, archivo):
        #Leemos el csv con pandas 
        self.df = pd.read_csv(archivo, sep=";")

    def normalizing (self):
        #Se cambia el nombre de las columnas para ajustarse al schema de la DB 
        new_columns = {
            "First Name":"first_name",
            "Last Name": "last_name",
            "Email":"email",
            "Application Date":"application_date",
            "Country":"country",
            "YOE":"yoe",
            "Seniority":"seniority",
            "Technology":"technology",
            "Code Challenge Score":"code_challenge_score",
            "Technical Interview Score":"technical_interview_score"
        }
        self.df.rename(columns=new_columns, inplace=True)
        #El csv no cuenta con la columna "Is_hired", la creamos con uso de pandas
        if (any(self.df["code_challenge_score"] >= 7)) and (any(self.df["technical_interview_score"] >= 7)) :
            self.df["is_hired"] = 1
        else:
            self.df["is_hired"] = 0
        
    def importing_db(self, engine):
        self.df.to_sql("candidates", con=engine, if_exists="replace", index_label="candidate_id")
        print("Succesfully Created")
