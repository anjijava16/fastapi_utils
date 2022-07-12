from fastapi import FastAPI, APIRouter,HTTPException
from typing import Optional,List
from pydantic import BaseModel
from sympy.polys.densetools import dmp_eval_tail

todo_router = APIRouter();


class Todo(BaseModel):
    name: str
    due_date: str
    description: str


# Create,Read,Update,Delete

store_todo = []


@todo_router.get("/")
async def home():
    return {'Hello': 'World'}

@todo_router.post('/todo/')
async def create_todo(todo:Todo):
    store_todo.append(todo)
    return todo

@todo_router.get('/todo/',response_model=List[Todo])
async def get_all_todos():
    return store_todo

@todo_router.get('/todo/{id}')
async def get_todo(id:int):
    try:
        return store_todo[id]
    except:
        raise HTTPException(status_code=404, detail='Todo Not Found')

@todo_router.put('/todo/{id}')
async def update_todo(id:int,todo:Todo):
    try:
        store_todo[id]=todo
        return store_todo[id]
    except:
        raise HTTPException(status_code=404, detail='Todo not Found ')

@todo_router.delete('/todo/{id}')
async def delete_todo(id: int):
    try:
        obj=store_todo[id]
        store_todo.pop(id)
        return obj
    except:
        raise HTTPException(status_code='404', detail='Todo Not Found')
