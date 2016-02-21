import shelve
import os

class Database:

    def __init__(self):
        directory = os.path.dirname(os.path.abspath(__file__))
        self.database = shelve.open(directory + "/../../database/database")

    def has_key(self, key):
        return self.database.has_key(key)

    def keys(self):
        return self.database.keys()

    def save(self, key, status):
        self.database[key] = status

    def retrieve(self, key):
        return self.database[key];

    def __str__(self):
        output = "database contents:\n"
        keys = self.database.keys()

        for key in keys:
            output += "   %s: %s\n" % (key, self.database[key])

        return output
