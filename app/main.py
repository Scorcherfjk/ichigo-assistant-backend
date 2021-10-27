# FastAPI
from fastapi import FastAPI

from app.services.mongoDB import MongoDB
from .routers import messages, intents, test

app = FastAPI(debug=True)

app.include_router(messages.router, prefix="/api")
app.include_router(intents.router, prefix="/api")
app.include_router(test.router)


@app.get('/')
def home():
    return {
        "version": "0.1.0",
        "name": "Ichigo API",
        "author": "FJavier De Freitas <ScorcherFJK>",
        "docs": "http://localhost:8000/docs"
    }


@app.on_event("startup")
def startup_event():
    global mdb
    mdb = MongoDB()


@app.on_event("shutdown")
def shutdown_event():
    mdb.close()