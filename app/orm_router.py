from fastapi import FastAPI, APIRouter

from fastapi.responses import HTMLResponse


orm_router = APIRouter()

# @orm_router.get('/book/res',response_class=HTMLResponse)