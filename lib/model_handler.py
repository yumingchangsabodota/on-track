from lib.mongo_db import MongoDb
from bson import ObjectId
from lib.obj_id_util import stringify_objid, objidify_str
from typing import Dict, List, Any, Union


class BaseModelHandler:
    def __init__(self, db_name: str = 'on_track'):
        self.db_name = db_name
        self.mongo_db = MongoDb()
        self.on_track_db = self.mongo_db.get_db(self.db_name)
        self.collection = self.mongo_db.get_collection(
            self.on_track_db, self.name)

    @stringify_objid('_id')
    def get(self):
        result = self.collection.find({})
        return result

    @stringify_objid('_id')
    def get_one(self, query):
        result = self.collection.find(query)
        return result

    @stringify_objid('_id')
    def create(self, data: List[Any]):
        result = self.collection.insert_many(data)
        return result.inserted_ids

    def update(self, data: List[Any]):
        modified_count = 0
        for d in data:
            id = ObjectId(d['_id'])
            del d['_id']
            result = self.collection.update_one(
                {"_id": id}, {"$set": d})
            modified_count += result.modified_count
        return {'modified_count': modified_count}
