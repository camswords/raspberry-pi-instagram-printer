import shelve
import os

class Repository:

    def __init__(self):
        directory = os.path.dirname(os.path.abspath(__file__))
        self.database = shelve.open(directory + "/../../database/database")

    def has_key(self, key):
        return self.database.has_key(key)

    def save(self, key, status):
        self.database[key] = status

    def retrieve(self, key):
        return self.database[key];
