import logging
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# from core import config
# from apis.api_v1.router_cleanings import cleaning_router
# from apis.api_v1.route_users import user_router
# from apis.api_v1.route_authentication import auth_router
from app.welcome_router import welcome_router
from app.pydantic_router import pydantic_router
from app.todo_router import todo_router
from app.multipart_router import multipart_router
from app.databaseapi.api.db_router import db_router

def include_routers(app):
    app.include_router(welcome_router)
    app.include_router(pydantic_router)
    app.include_router(todo_router)
    app.include_router(multipart_router)
    app.include_router(db_router)
    # app.include_router(user_router)
    # app.include_router(auth_router)


def get_application():
    # app = FastAPI(title=config.PROJECT_NAME, version=config.VERSION)
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins = ['127.0.0.1'],
        allow_credentials = True,
        allow_methods = ["*"],
        allow_headers = ["*"],
    )
    # app.add_event_handler("startup",tasks.create_start_app_handler(app))
    # app.add_event_handler("shutdown",tasks.create_stop_app_handler(app))
    include_routers(app)
    # #logging
    log = logging.getLogger("uvicorn")
    log.setLevel(logging.DEBUG)
    command_line_handler = logging.StreamHandler()
    command_line_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(levelname)s- api - %(asctime)s - %(message)s')
    command_line_handler.setFormatter(formatter)
    log.addHandler(command_line_handler)
    return app


app = get_application()

@app.get("/")
def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=4747)