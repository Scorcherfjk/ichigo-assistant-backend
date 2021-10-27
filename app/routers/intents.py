from fastapi import APIRouter, status
from app.controllers.intent import IntentController

from app.models.intents import DeleteIntentModel, IntentModel, ListIntentModel, ResponseIntentModel, UpdateIntentModel

router = APIRouter(
    prefix="/intents",
    tags=["Api Intents"]
)


@router.get("/", response_model=ListIntentModel, status_code=status.HTTP_200_OK)
def list_intents():
    """
    # Intents API

    This endpoind list the intents

    Return
     -  the id

    """

    controller = IntentController()
    response = controller.read_many_intents()

    return ListIntentModel(intents=response)


@router.post("/", response_model=ResponseIntentModel, status_code=status.HTTP_201_CREATED)
def create_intent(intent: IntentModel):
    """
    # Intents API

    This endpoind create an intent

    Return
     -  the id

    """

    controller = IntentController()
    response = controller.create_intent(intent.dict())

    return ResponseIntentModel(id=response)


@router.put("/", response_model=IntentModel, status_code=status.HTTP_201_CREATED)
def update_intent(intent: UpdateIntentModel):
    """
    # Intents API

    This endpoind update the intent

    Return
     -  the id

    """

    return {"hello": "world"}


@router.delete("/", response_model=ResponseIntentModel, status_code=status.HTTP_200_OK)
def delete_intent(intent: DeleteIntentModel):
    """
    # Intents API

    This endpoind delete the intent

    Return
     -  the id

    """
    controller = IntentController()
    response = controller.delete_intent(intent.id)

    return ResponseIntentModel(id=response)