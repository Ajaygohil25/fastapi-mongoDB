from pymongo import MongoClient

uri = "mongodb+srv://ajayginexture:ajay-admin@cluster0.s1xscly.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri)

db = client.todo_db

collection_name = db["todo_collection"]