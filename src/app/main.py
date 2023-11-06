from fastapi import FastAPI
from src.infrastructure.exceptions.error_handler import ErrorHandler
from src.domain.models.base_entity import init
from src.app.routers.api.user import user_router
from src.app.routers.api.auth import auth_router

app = FastAPI()

app.add_middleware(ErrorHandler)

app.include_router(auth_router)

app.include_router(user_router)

init()