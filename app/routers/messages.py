from fastapi import APIRouter, status

from app.models.messages import UserMessageModel, AssistantMessageModel
from app.controllers.assistant import AssistantController

router = APIRouter(
    prefix="/messages",
    tags=["Api Messages"]
)



@router.post("/", response_model=AssistantMessageModel, status_code=status.HTTP_200_OK)
def messages(message: UserMessageModel):
    """
    # Message API

    This endpoind receive the message from the user and reply

    Return
     - Message from the NLP Model 

    """

    controller = AssistantController(message)
    response = controller.process()

    return response
