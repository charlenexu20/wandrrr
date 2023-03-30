#from queries.journal_entries import
from fastapi import APIRouter, Depends
from auth.auth_bearer import JWTBearer

router = APIRouter()


post = [
    {
        "id": 1,
        "title": "title1",
        "location": "location1"
    },
    {
        "id": 2,
        "title": "title2",
        "location": "location2"
    }
]

@router.get("/wandrrrs/", tags=["post"])
def get_list():
      return{
            "data": post
      }

@router.get("/wandrrrs/{id}", tags=["post"])
def get_post(id : int):

        return {
            "data": post
        }
@router.put("/wandrrrs/{id}")
def edit_post(id : int):
    return()

@router.delete("/wandrrrs/{id}")
def delete_post(id : int):
    return()

@router.post("/wandrrrs/", dependencies=[Depends(JWTBearer())])
def create_post():
    return()