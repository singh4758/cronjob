from ..database.database import Database


class Watcher:
    def __init__(self):
        self.db = Database()

        self.collection_name = 'Watcher'  # collection name
    
    def find(self, query):  # find all
        return self.db.find(query, self.collection_name)