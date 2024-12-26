from fastapi import APIRouter
from config.database import collection_name
from models.todos_models import Todo
from schemas.todos_schema import todo_serializer,todos_serializer

todo_api_router = APIRouter()


#Retrieve 
@todo_api_router.get("/")
async def get_todos():
    todod = todos_serializer(collection_name.find())
    return {"status":"ok","data":"todos"}