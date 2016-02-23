import shelve
import os
from support_team import SupportTeam

class Database:

    def query_db(self, callable):
        directory = os.path.dirname(os.path.abspath(__file__))
        db = shelve.open(directory + "/../../database/database")
        result = callable(db)
        db.close()
        return result

    def assign_to_db(self, key, callable):
        directory = os.path.dirname(os.path.abspath(__file__))
        db = shelve.open(directory + "/../../database/database")
        db[key] = callable(db)
        db.close()

    def has_key(self, key):
        return self.query_db(lambda db: db.has_key(key))

    def keys(self):
        return self.query_db(lambda db: db.keys())

    def save(self, key, status):
        SupportTeam.notify("*** saving %s with status %s ***" % (key, status))
        self.assign_to_db(key, lambda db: status)

    def retrieve(self, key):
        return self.query_db(lambda db: db[key])

    def __str__(self):
        def to_str(db):
            output = "database contents:\n"
            keys = db.keys()

            for key in keys:
                if "latest-media" == key:
                    output += "   %s: %s\n" % (key, db[key])
                else:
                    output += "   %s: %s\n" % (key, db[key]["status"])

            return output

        return self.query_db(to_str)
