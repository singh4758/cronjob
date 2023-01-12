from ..database.database import Database


class User:
    def __init__(self):
        self.db = Database()
        self.collection_name = 'User'  # collection name
    
    def find_one(self, query):  # find all
        return self.db.find_one(query, self.collection_name)