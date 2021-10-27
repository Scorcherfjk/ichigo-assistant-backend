from fastapi import APIRouter, status

from app.services.mongoDB import MongoDB

router = APIRouter(
    prefix="/test",
    tags=["Test"]
)



@router.post("/create", status_code=status.HTTP_200_OK)
def create():
    """
    # Message API

    This endpoind receive the message from the user and reply

    Return
     - Message from the NLP Model 

    """

    mdb = MongoDB('test')
    response = mdb.create({"hello": "world"})

    return {"id": response }
