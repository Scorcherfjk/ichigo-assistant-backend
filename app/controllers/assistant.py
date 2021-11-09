from textblob import TextBlob
from app.models.messages import AssistantMessageModel, UserMessageModel
from app.services.mongoDB import MongoDB


class AssistantController():

    def __init__(self):
        self._db = MongoDB()
        self._db.set_collection('intents')

    def process(self, message: UserMessageModel):

        # En este punto debe llamar la modelo
        # El modelo devueve la intención
        intent = message.content

        # Se evalua el sentimiento del mensajes recibido
        analysis = TextBlob(message.content)
        language = analysis.detect_language()
        if language == 'en':
            analysis_ready = analysis
        else:
            analysis_ready = analysis.translate(to='en')

        sentiment = ''
        if analysis_ready.sentiment.polarity > 0:
            sentiment = 'positive'
        elif analysis_ready.sentiment.polarity == 0:
            sentiment = 'neutral'
        else:
            sentiment = 'negative'

        # Se busca en la base de datos los mensajes que corresponden a la intención y al sentimiento.
        # la respuesta deberia ser { "intent": "", "response": ["", "", ""] response_type: "", sentiment: "" }
        dialog = self._db.read_many(
            {"intent": {"$in": [intent, "no entiendo"]}, "sentiment": {"$in": [sentiment, "any"]}})

        for doc in dialog:
            doc_response = doc
            message_response = doc['response'][0]
            break

        # Se almacena en la base de datos
        # { "user_message": "", "assistant_message": "", "intent": "", "confidence": "", "created_at": "" }
        self._db.set_collection('logs')
        self._db.create({
            "user_message": message.content,
            "assistant_message": message_response["message"],
            "intent": doc_response["intent"],
            "confidence": 0.0,
            "created_at": message.createdTimestamp
        })

        # Se estructura la respuesta y responde.
        response = None
        response = AssistantMessageModel(
            message=message_response["message"],
            has_reaction=message_response["has_reaction"],
            reaction=message_response["reaction"]
        )

        return response
