from pymongo.mongo_client import MongoClient
import pandas as pd
import numpy as np

#Url

uri = "mongodb+srv://devraj:FE9CTfkKmtCGHJXH@cluster0.ulndc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

#create a new client
client = MongoClient(uri)

#Defining Database
#Collection Name in MongoDB

DATABASE_NAME = 'newDatabase'
COLLECTION_NAME = 'waferfault'

df = pd.read_csv("C:\Users\Lenovo\Desktop\sensorproject\notebooks\wafer_23012020_041211 (3).csv")

df.head()

# Droping useless Columns
df = df.drop("Unnamed: 0",axis = 1)

#Converting Json file for MongoDB
import json
json_record = list(json.loads(df.T.to_json()).values())

#Uploading Data in MongoDB
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)


