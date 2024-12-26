from pymongo import MongoClient

MONGODB_URL = "mongodb+srv://hari:hari2004@cluster0.jjqjl.mongodb.net/"

client = MongoClient(MONGODB_URL)

db = client.Todo_App

collection_name = db['todos_app']