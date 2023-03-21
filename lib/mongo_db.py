
import os
from pymongo import MongoClient


class MongoDb:
    def __init__(self):
        self._host = os.getenv("MONGO_HOST", None).split(",")
        self._port = int(os.getenv("MONGO_PORT", None))
        self._username = os.getenv("MONGO_USER", None)
        self._password = os.getenv("MONGO_PASSWORD", None)
        self._db_name = os.getenv("DB_NAME", None)
        self._replicaset = os.getenv("REPLICASET", None)

        self._mongo_client = MongoClient(host=self._host,
                                         port=self._port,
                                         username=self._username,
                                         password=self._password,
                                         replicaSet=self._replicaset,
                                         authSource=self._db_name)

    def get_db(self, db_name: str):
        return self._mongo_client[db_name]

    def get_collection(self, mongo_db: MongoClient, collection: str):
        return mongo_db[collection]
