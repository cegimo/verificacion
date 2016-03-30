from pymongo import MongoClient


class dbConnection:
    def __init__(self, collection):
        self.client = MongoClient('localhost', 27017)


        self.db = self.client.prueba
        self.collection = self.db[collection]


        print 'Conexion establecida con la BD'


