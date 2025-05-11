from bson import ObjectId
from fastapi import APIRouter
from starlette.responses import JSONResponse
from config.database import collection_name
from schemas.schemas import list_of_serials
from pydantic_models.todo_model import Todo
router = APIRouter()

@router.post("/add-post")
async def add_post(todo: Todo):
    """ This API add post in db."""
    collection_name.insert_one(dict(todo))
    return JSONResponse({
            "info":"inserted successfully"
        },
        status_code= 201
    )

@router.get("/")
async def get_all_post():
    """ This API get all posts. """
    todos =  list_of_serials(collection_name.find())
    return todos

@router.put("/{id}")
async def update_post(id: str, todo: Todo):
    """ This API update post in DB."""
    collection_name.find_one_and_update({"_id":ObjectId(id)}, {"$set":dict(todo)})
    return JSONResponse({
        "info": "updated successfully"
    },
        status_code=200
    )

@router.delete("/{id}")
async def delete_post(id: str):
    """ This API delete the post in the DB. """
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return JSONResponse({
        "info": "Deleted successfully"
    },
        status_code=200
    )

