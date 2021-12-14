from fastapi import APIRouter, status, HTTPException
from app.controllers.intent import IntentController

from app.models.intents import DeleteIntentModel, IntentModel, ListIntentModel, ResponseIntentModel, UpdateIntentModel

router = APIRouter(
    prefix="/intents",
    tags=["Api Intents"]
)


@router.get("/", response_model=ListIntentModel, status_code=status.HTTP_200_OK)
def list_intents():
    """
    ## list intents API

    This endpoind list the intents

    """

    controller = IntentController()
    response = controller.read_many_intents()

    return ListIntentModel(intents=response)


@router.post("/", response_model=ResponseIntentModel, status_code=status.HTTP_201_CREATED)
def create_intent(intent: IntentModel):
    """
    ## Create intent API

    This endpoind create an intent

    """

    controller = IntentController()
    response = controller.create_intent(intent.dict())

    return ResponseIntentModel(id=response)


@router.put("/", response_model=IntentModel, status_code=status.HTTP_201_CREATED)
def update_intent(intent: UpdateIntentModel):
    """
    ## update intent API

    This endpoind update the intent

    """

    controller = IntentController()
    response = controller.update_intent(intent.dict())

    if response:
        doc = controller.read_intent(intent.id)
        return doc
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Ocurrio un error al intentar actualizar la intención")


@router.delete("/", response_model=ResponseIntentModel, status_code=status.HTTP_200_OK)
def delete_intent(intent: DeleteIntentModel):
    """
    ## delete intent API

    This endpoind delete the intent

    """
    controller = IntentController()
    response = controller.delete_intent(intent.id)

    if response:
        return ResponseIntentModel(id=intent.id)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Ocurrio un error al intentar eliminar la intención")
