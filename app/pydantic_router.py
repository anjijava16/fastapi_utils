from fastapi import FastAPI, APIRouter
from typing import Optional
from pydantic import BaseModel


class Package(BaseModel):
    name: str
    number: str
    description: Optional[str] = None

class PackageIn(BaseModel):
    secret_id:int
    name: str
    number: str
    description: Optional[str] = None

pydantic_router = APIRouter()


@pydantic_router.get("/pydantic")
async def hello_world():
    return {"hello": "world"}


@pydantic_router.post("/package/")
async def make_package(package:Package):
    return package


@pydantic_router.post("/response_package/",response_model=Package,response_model_exclude_unset=True)
async def response_package(packageIn:PackageIn):
    return packageIn

@pydantic_router.post("/response_package_include/",response_model=Package,response_model_include={"description"})
async def response_package_include(packageIn:PackageIn):
    return packageIn