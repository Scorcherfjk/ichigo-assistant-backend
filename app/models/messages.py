# Python
from typing import Optional

# Pydantic
from pydantic import BaseModel, Field


class UserMessageModel(BaseModel):
    id: str = Field(...,
                    min_length=1,
                    max_length=100,
                    title="ID",
                    description="Identificador del mensaje",
                    )
    content: str = Field(...,
                         min_length=1,
                         max_length=250,
                         title="Contenido",
                         description="Mensaje enviado por el usuario",
                         )
    type: str = Field(...,
                      min_length=1,
                      max_length=20,
                      title="Tipo de mensaje",
                      description="Tipo de mensaje dependiendo del canal"
                      )
    username: str = Field(...,
                          min_length=1,
                          max_length=50,
                          title="Nombre de Usuario",
                          description="Apodo del usuario que envió el mensaje"
                          )
    createdTimestamp: int = Field(...,
                                  gt=1,

                                  title="Fecha de envio",
                                  description="Timestamp en la que el usuario envió el mensaje"
                                  )

    class Config:
        schema_extra = {
            "example": {
                "id": '901298500053110804',
                "content": 'hola',
                "type": 'dm',
                "username": 'pepito',
                "createdTimestamp": 1634956707729
            }
        }


class AssistantMessageModel(BaseModel):
    message: str = Field(...,
                         min_length=1,
                         max_length=300,
                         title="Mensaje",
                         description="Mensaje en respuesta al usuario"
                         )
    has_reaction: bool = Field(
                         default=False,
                         title="Tiene Reacción",
                         description="Indica si el mesaje cuenta con reacción o no"
                         )
    
    reaction: Optional[str] = Field(default=None,
                         min_length=1,
                         max_length=10,
                         title="Reacción",
                         description="Emoji que reaccionará el asistente"
                         )
