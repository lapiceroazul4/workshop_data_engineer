import pymysql
import json 

with open('db_config.json', 'r') as json_file:
    data = json.load(json_file)
    usuario = data["user"]
    password = data["passwd"]
    server = data["server"]
    database = data["database"]

class connecting_database():

  def __init__ (self):
    self.connection = pymysql.connect(
        host=server,
        user=usuario,
        passwd=password,
        db=database

    )
    self.cursor = self.connection.cursor()
    print("Connection succesfully")

a = connecting_database()