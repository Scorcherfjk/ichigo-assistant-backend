from typing import Optional
from enum import Enum

# Pydantic
from pydantic import BaseModel, Field

from app.models.messages import AssistantMessageModel


class Sentiment(Enum):
    positive = "positive"
    neutral = "neutral"
    negative = "negative"
    any = "any"


class ResponseType(Enum):
    multiline = "multiline"
    random = "random"


class IntentModel(BaseModel):
    id: Optional[str] = Field(
        min_length=24,
        max_length=24,
        title="Id de la Intención",
        description="id generado por MongoDB del documento")
    intent: str = Field(
        ...,
        min_length=1,
        max_length=50,
        title="Nombre de la Intención",
        description="El nombre por el que se identificará la intención")
    response: list[AssistantMessageModel] = Field(
        ...,
        min_items=1,
        max_items=10,
        title="Lista de respuestas",
        description="Los diferentes ejemplos de respuesta de la intención")
    response_type: ResponseType = Field(
        ...,
        title="Tipo de respuesta",
        description="El tipo de respuesta de la intención")
    sentiment: Sentiment = Field(
        ...,
        title="Sentimiento",
        description="El sentimiento al que se asigna las respuestas")

    class Config:
        use_enum_values = True
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
    id: str = Field(
        ...,
        min_length=24,
        max_length=24,
        title="Id de la Intención",
        description="identificador de la intención modificada")


class ListIntentModel(BaseModel):
    intents: list[IntentModel] = Field(
        ...,
        title="Lista de Intenciones",
        description="Un listado de las intenciones existentes")


class UpdateIntentModel(BaseModel):
    id: str = Field(
        ...,
        min_length=24,
        max_length=24,
        title="Id del documento",
        description="Identificador del documento que será editado")
    intent: Optional[str] = Field(
        min_length=1,
        max_length=50,
        title="Nombre del Intención",
        description="Nuevo nombre de intención")
    response: Optional[list[AssistantMessageModel]] = Field(
        min_items=1,
        max_items=10,
        title="Lista de respuestas",
        description="Nuevo listado de respuestas")
    response_type: Optional[ResponseType] = Field(
        title="Tipo de respuesta",
        description="Nuevo tipo de respuestas")
    sentiment: Optional[Sentiment] = Field(
        title="Sentimiento",
        description="Nuevo sentimiento asignado a la respuesta")

    class Config:
        use_enum_values = True
        schema_extra = {
            "example": {
                "id": "617947a59ed4b513dab1cfb8",
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


class DeleteIntentModel(BaseModel):
    id: str = Field(
        ...,
        min_length=24,
        max_length=24,
        title="Id de documento",
        description="Identificador del documento que será eliminado")
