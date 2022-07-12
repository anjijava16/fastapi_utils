from fastapi import FastAPI, APIRouter



welcome_router = APIRouter()


@welcome_router.get("/welcome", status_code=200)
def welcome():
    return "Welcome to FastAPI"


@welcome_router.get("/", status_code=200)
def root() -> dict:
    """
    Root GET
    """
    return {"msg": "Hello, World!"}
'''

http://localhost:4747/componentid/100

'''
@welcome_router.get("/componentid/{component_id}")
async def get_component(component_id):
    return {"component_id":component_id}


# Path Parameter
'''
http://localhost:4747/readcomponent?number=100&text=welcome

'''
@welcome_router.get("/componentid_int/{component_id}")
async def get_component_int(component_id:int):
    return {"comp_id":component_id}

# Query Parameter
@welcome_router.get("/readcomponent")
async def read_component(number:int,text:str):
    return {"number":number,"text":text}

