from fastapi import FastAPI
from src.infrastructure.exceptions.error_handler import ErrorHandler
from src.infrastructure.configs.enviroment import get_enviroment_settinngs
from src.domain.models.base_entity import init
from src.app.routers.api.auth import auth_router
from src.app.routers.api.user import user_router
from src.app.routers.api.file import file_router

env = get_enviroment_settinngs()

app = FastAPI()

app.title = env().APP_NAME

app.version = env().API_VERSION

app.description = env().APP_DESCRIPTION

app.add_middleware(ErrorHandler)

app.include_router(auth_router)

app.include_router(user_router)

app.include_router(file_router)

init()