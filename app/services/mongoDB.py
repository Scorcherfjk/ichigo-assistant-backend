from uuid import uuid1
from bson.objectid import ObjectId
from pymongo import MongoClient
import os


class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """

        if cls not in cls._instances:

            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class MongoDB(metaclass=SingletonMeta):
    _connection_string = f"mongodb://{os.environ.get('DB_USER')}:{os.environ.get('DB_PASS')}@{os.environ.get('DB_HOST')}/{os.environ.get('DB_NAME')}?ssl=true&replicaSet=atlas-y5g1pb-shard-0&authSource=admin&retryWrites=true&w=majority"

    def __init__(self, collection = 'intents') -> None:
        self._id = uuid1()
        self._client = MongoClient(self._connection_string)
        self._db = self._client[os.environ.get('DB_NAME')]
        self._collection = self._db[collection]
        print(f"Connection {self._id} was created")

    def set_collection(self, collection) -> None:
        self._collection = self._db[collection]

    def read(self, id, projection = None):
        return self._collection.find_one(filter={"_id": ObjectId(id)}, projection=projection)

    def read_many(self, filter = None, projection = None, sort = None):
        return self._collection.find(filter=filter, projection=projection, sort=sort)

    def create(self, payload):
        doc = self._collection.insert_one(payload)
        return str(doc.inserted_id)

    def create_many(self, payload):
        docs = self._collection.insert_many(payload)
        return docs.inserted_ids

    def update(self, id, newvalues):
        self._collection.update_one({"_id": ObjectId(id)}, {"$set": newvalues})
        return True

    def update_many(self, query, newvalues):
        docs = self._collection.update_many(query, newvalues)
        return docs.modified_count

    def delete(self, id):
        self._collection.delete_one({"_id": ObjectId(id)})
        return True

    def delete_many(self, query):
        docs = self._collection.delete_many(query)
        return docs.deleted_count

    def close(self):
        print(f"Connection {self._id} was destroyed")
        self._client.close()
