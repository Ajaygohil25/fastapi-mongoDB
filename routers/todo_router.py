from fastapi import APIRouter
from starlette.responses import JSONResponse

from config.database import collection_name
from schemas.schemas import list_of_serials
from pydantic_models.todo_model import Todo
router = APIRouter()


@router.post("/add-post")
async def add_post(todo: Todo):
    """ This method add post in db."""
    collection_name.insert_one(dict(todo))
    return JSONResponse({
            "info":"inserted successfully"
        },
        status_code= 201
    )

@router.get("/")
async def get_all_post():
    """ This method get all posts. """
    todos =  list_of_serials(collection_name.find())
    return todos