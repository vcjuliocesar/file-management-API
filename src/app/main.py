from fastapi import FastAPI
from src.infrastructure.configs.database import engine,Base


app = FastAPI()

Base.metadata.create_all(bind=engine)