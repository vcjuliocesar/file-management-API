from fastapi import FastAPI
from src.infrastructure.configs.database import engine,Base,DATABASE_URL

Base.metadata.create_all(bind=engine)

print(DATABASE_URL)