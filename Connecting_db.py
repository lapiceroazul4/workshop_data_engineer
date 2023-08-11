import pymysql
import json 

with open('db_config.json', 'r') as json_file:
    data = json.load(json_file)
    usuario = data["user"]
    password = data["passwd"]

class connecting_database():

  def __init__ (self):
    self.connection = pymysql.connect(
        host="localhost",
        user=usuario,
        passwd=password,
        db="workshop"

    )
    self.cursor = self.connection.cursor()
    print("Connection succesfully")

a = connecting_database()