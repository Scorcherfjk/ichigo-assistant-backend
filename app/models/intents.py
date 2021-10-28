from typing import Optional
from enum import Enum

# Pydantic
from pydantic import BaseModel, Field

from app.models.messages import AssistantMessageModel


class Sentiment(Enum):
    positive = "positive"
    neutral = "neutral"
    negative = "negative"


class ResponseType(Enum):
    multiline = "multiline"
    random = "random"


class IntentModel(BaseModel):
    id: Optional[str] = Field(min_length=24, max_length=24, title="Id de la Intención")
    intent: str = Field(..., min_length=1, max_length=50,
                        title="Nombre de la Intención")
    response: list[AssistantMessageModel] = Field(..., min_items=1,
                                max_items=10, title="Lista de respuestas")
    response_type: str = Field(..., title="Tipo de respuesta")
    sentiment: str = Field(..., title="Sentimiento")

    class Config:
        schema_extra = {
            "example": {
                "intent": 'saludo',
                "response": [{
                    "message": "hola",
                    "has_reaction": True,
                    "reaction": "👍🏻"
                }],
                "response_type": "random",
                "sentiment": "positive"
            }
        }

class ResponseIntentModel(BaseModel):
    id: str = Field(..., min_length=24, max_length=24, title="Id de la Intención")


class ListIntentModel(BaseModel):
    intents: list[IntentModel] = Field(..., title="Lista de Intenciones")


class UpdateIntentModel(BaseModel):
    id: str = Field(..., min_length=24, max_length=24,
                    title="Id del documento")
    intent: Optional[str] = Field(
        min_length=1, max_length=50, title="Nombre del Intención")
    response: Optional[list[AssistantMessageModel]] = Field(
        min_items=1, max_items=10, title="Lista de respuestas")
    response_type: Optional[str] = Field(title="Tipo de respuesta")
    sentiment: Optional[str] = Field(title="Sentimiento")

    class Config:
        schema_extra = {
            "example": {
                "id": "617947a59ed4b513dab1cfb8",
                "intent": 'saludo',
                "response": ["hola"],
                "response_type": "random",
                "sentiment": "positive"
            }
        }


class DeleteIntentModel(BaseModel):
    id: str = Field(..., min_length=24, max_length=24, title="Id de documento")
