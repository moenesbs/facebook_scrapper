import imp
import pymongo
import uvicorn
from fastapi import FastAPI
from scrapper import scrap
from utils import logger
import json
from dotenv import load_dotenv
import os

load_dotenv()
try : 
    client = pymongo.MongoClient(os.getenv("DB_URL"))
    document = client['Facebook']['Google']
except pymongo.errors.ConnectionFailure as e:
    raise f"Could not connect to server {e}"

app = FastAPI()

@app.post("/scrap")
def main():
    data = scrap()
    for post in json.loads(data):
        document.insert_one(post)
    logger.info('Data added to the DataBase')
    return {
        "message": f"Added posts to the DataBase",
        "data" : data
        }
if __name__ =='__main__':
     uvicorn.run("main:app", host="0.0.0.0", port=80, log_level="info")