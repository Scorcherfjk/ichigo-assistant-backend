# FastAPI
from fastapi import FastAPI
from app.models.docs import DocsModel

from app.services.mongoDB import MongoDB
from .routers import messages, intents

app = FastAPI(debug=True)

app.include_router(messages.router, prefix="/api")
app.include_router(intents.router, prefix="/api")


@app.get('/', response_model=DocsModel)
def home():
    return DocsModel(
        version="0.1.0",
        name="Ichigo API",
        author="FJavier De Freitas <ScorcherFJK>",
        docs="http://localhost:8000/redoc"
    )


@app.on_event("startup")
def startup_event():
    global mdb
    mdb = MongoDB()


@app.on_event("shutdown")
def shutdown_event():
    mdb.close()
