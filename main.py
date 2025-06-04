from fastapi import FastAPI
from pymongo.mongo_client import MongoClient
from routers.todo_router import router

app = FastAPI()
app.include_router(router)