#mongodb://<dbuser>:<dbpassword>@ds027425.mlab.com:27425/techfood
import mongoengine
import json

#mongodb://<dbuser>:<dbpassword>@ds161048.mlab.com:61048/kingcua

host = "ds161048.mlab.com"
port = 61048
db_name = "kingcua"
user_name = "cuong"
password = "cuong"

def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
   return [json.loads(item.to_json()) for item in l]

def item2json(item):
   return json.loads(item.to_json())