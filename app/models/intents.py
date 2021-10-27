from typing import Optional
from enum import Enum

# Pydantic
from pydantic import BaseModel, Field


class Sentiment(Enum):
    positive = "positive"
    neutral = "neutral"
    negative = "negative"


class ResponseType(Enum):
    multiline = "multiline"
    random = "random"


class IntentModel(BaseModel):
    intent: str = Field(..., min_length=1, max_length=50,
                        title="Nombre de la Intención")
    response: list[str] = Field(..., min_items=1,
                                max_items=10, title="Lista de respuestas")
    response_type: str = Field(..., title="Tipo de respuesta")
    sentiment: str = Field(..., title="Sentimiento")

    class Config:
        schema_extra = {
            "example": {
                "intent": 'saludo',
                "response": ["hola"],
                "response_type": "random",
                "sentiment": "positive"
            }
        }

class ResponseIntentModel(BaseModel):
    id: str = Field(min_length=1, max_length=50, title="Id de la Intención")


class ListIntentModel(BaseModel):
    intents: list[IntentModel] = Field(..., title="Lista de Intenciones")


class UpdateIntentModel(BaseModel):
    id: str = Field(..., min_length=1, max_length=100,
                    title="Id del documento")
    intent: Optional[str] = Field(
        min_length=1, max_length=50, title="Nombre del Intención")
    response: Optional[list[str]] = Field(
        min_items=1, max_items=10, title="Lista de respuestas")
    respose_type: Optional[ResponseType] = Field(title="Tipo de respuesta")
    sentiment: Optional[Sentiment] = Field(title="Sentimiento")

    class Config:
        schema_extra = {
            "example": {
                "id": "jsfakfaslkasjldjas",
                "intent": 'saludo',
                "response": ["hola"],
                "response_type": "random",
                "sentiment": "positive"
            }
        }


class DeleteIntentModel(BaseModel):
    id: str = Field(..., min_length=1, max_length=100, title="Id de documento")
