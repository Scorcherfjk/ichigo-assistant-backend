from typing import Dict

from bson.objectid import ObjectId
from app.models.intents import IntentModel
from app.services.mongoDB import MongoDB


class IntentController():

    def __init__(self) -> None:
        self._db = MongoDB()
        self._db.set_collection('intents')

    def read_many_intents(self) -> list:
        docs = self._db.read({})
        container = []
        for doc in docs:
            container.append(IntentModel(
                id=str(doc['_id']),
                intent=doc['intent'],
                response=doc['response'],
                response_type=doc['response_type'],
                sentiment=doc['sentiment'],
            ))

        return container
        

        
    def read_intent(self, id):
        doc = self._db.read({"_id": ObjectId(id)})
        model = IntentModel(
                id=str(doc['_id']),
                intent=doc['intent'],
                response=doc['response'],
                response_type=doc['response_type'],
                sentiment=doc['sentiment'],
            )
        return model
        

    def create_intent(self, payload: Dict) -> str:
        return self._db.create(payload)

    def update_intent(self, payload):
        pass

    def delete_intent(self, payload):
        pass