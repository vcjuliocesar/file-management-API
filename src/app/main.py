from fastapi import FastAPI
from src.domain.models.base_entity import init
from src.app.routers.api.user import user_router

app = FastAPI()

app.include_router(user_router)

init()