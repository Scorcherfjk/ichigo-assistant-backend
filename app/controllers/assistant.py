from textblob import TextBlob
from app.models.messages import AssistantMessageModel, UserMessageModel
from app.services.mongoDB import MongoDB


class AssistantController():

    def __init__(self):
        self._db = MongoDB()
        self._db.set_collection('messages')

    def process(self, message: UserMessageModel):

        # En este punto debe llamar la modelo
        # El modelo devueve la intención

        # Se evalua el sentimiento del mensajes recibido
        analysis = TextBlob(message.content)
        language = analysis.detect_language()
        if language == 'en':
            analysis_ready = analysis
        else:
            analysis_ready = analysis.translate(to='en')

        # Se busca en la base de datos los mensajes que corresponden a la intención y al sentimiento.
        # la respuesta deberia ser { "intent": "", "response": ["", "", ""] response_type: "", sentiment: "" }

        # Se almacena en la base de datos
        # { "user_message": "", "assistant_message": "", "intent": "", "confidence": "", "created_at": "" }

        # Se estructura la respuesta y responde.
        response = None
        if analysis_ready.sentiment.polarity > 0:
            response = AssistantMessageModel(
                message="holi", has_reaction=True, reaction="🤖")
        elif analysis_ready.sentiment.polarity == 0:
            response = AssistantMessageModel(
                message="hola", has_reaction=False)
        else:
            response = AssistantMessageModel(
                message="me bajas el tonito", has_reaction=True, reaction="😡")

        return response
