from app.models.intents import IntentModel
from app.services.mongoDB import MongoDB


class IntentController():

    def __init__(self) -> None:
        self._db = MongoDB()
        self._db.set_collection('intents')

    # Ready
    def read_many_intents(self) -> list:
        docs = self._db.read_many()
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
        

    # Ready
    def read_intent(self, id):
        doc = self._db.read(id)
        model = IntentModel(
                id=str(doc['_id']),
                intent=doc['intent'],
                response=doc['response'],
                response_type=doc['response_type'],
                sentiment=doc['sentiment'],
            )
        return model
        
    # Ready
    def create_intent(self, payload) -> str:
        payload.pop('id')
        return self._db.create(payload)

    
    def update_intent(self, payload):
        id = payload.pop("id")
        new_payload = dict()
        for d in payload.items():
            if d[1] is not None:
                new_payload[d[0]] = d[1]

        return self._db.update(id, new_payload)

    def delete_intent(self, id):
        return self._db.delete(id)