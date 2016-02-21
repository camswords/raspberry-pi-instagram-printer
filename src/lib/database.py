import shelve
import os

class Database:

    def with_db(self, callable):
        directory = os.path.dirname(os.path.abspath(__file__))
        db = shelve.open(directory + "/../../database/database")
        result = callable(db)
        db.close()
        return result

    def has_key(self, key):
        return self.with_db(lambda db: db.has_key(key))

    def keys(self):
        return self.with_db(lambda db: db.keys())

    def save(self, key, status):
        self.with_db(lambda db: db[key] = status)

    def retrieve(self, key):
        return self.with_db(lambda db: db[key])

    def __str__(self):
        def to_str(db):
            output = "database contents:\n"
            keys = db.keys()

            for key in keys:
                output += "   %s: %s\n" % (key, db[key])

            return output

        return self.with_db(to_str)
