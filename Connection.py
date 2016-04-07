from pymongo import MongoClient


class Connection:
    def __init__(self, db_name):
        self._conn = MongoClient("localhost", 27017)
        self._db = self._conn[db_name]

    def collection(self, name=""):
        return self._db[name]