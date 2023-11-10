from fastapi import FastAPI, HTTPException
from src.infrastructure.exceptions.error_handler import ErrorHandler
from src.infrastructure.exceptions.not_found_exception_handler import not_found_exception_handler
from src.infrastructure.configs.enviroment import get_enviroment_settinngs
from src.domain.models.base_entity import init
from src.app.routers.api.index import index_router
from src.app.routers.api.auth import auth_router
from src.app.routers.api.user import user_router
from src.app.routers.api.file import file_router

env = get_enviroment_settinngs()

app = FastAPI()

app.title = env().APP_NAME

app.version = env().API_VERSION

app.description = env().APP_DESCRIPTION

app.add_middleware(ErrorHandler)

app.add_exception_handler(HTTPException,not_found_exception_handler)

app.include_router(index_router)

app.include_router(auth_router)

app.include_router(user_router)

app.include_router(file_router)

init()