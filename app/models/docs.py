# Pydantic
from pydantic import BaseModel, Field

class DocsModel(BaseModel):
  version: str = Field(default="0.1.0")
  name: str = Field(default="Ichigo API")
  author: str = Field(default="FJavier De Freitas <ScorcherFJK>")
  docs: str = Field(default="http://localhost:8000/redoc")


