from datetime import datetime
from pymongo import MongoClient
from bson import ObjectId
import sys
from src.config.configuartions import config

sys.path.append("../../src")

class Database(object):
    def __init__(self):
        self.client = MongoClient(config['db']['mongo_url'])  # configure db url
        self.db = self.client[config['db']['db_name']]  # configure db name

    def find(self, query, collection_name):  # find one docs to db
        response = self.db[collection_name].find(query)
        return response
    
    def find_one(self, query, collection_name):  # find one docs to db
        response = self.db[collection_name].find_one(query)
        return response

