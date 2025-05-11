from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()
DB_USER_NAME =  os.getenv("DB_USER_NAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")

uri = f"mongodb+srv://{DB_USER_NAME}:{DB_PASSWORD}@cluster0.s1xscly.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri)

db = client.todo_db

collection_name = db["todo_collection"]