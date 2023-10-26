import os
from pydantic_settings import BaseSettings

def get_env_file() -> str:
    env_file = os.getenv('ENV')
    return f".env.{env_file}" if env_file else ".env" 

def get_enviroment():
    return Enviroment;

class Enviroment(BaseSettings):
    API_VERSION:str
    APP_NAME:str
    APP_DESCRIPTION:str | None
    DATABASE_ENGINE:str
    DATABASE_NAME:str
    DATABASE_USER:str
    DATABASE_PASSWORD:str
    DATABASE_HOST:str
    DATABASE_PORT:int
    
    class Config:
        env_file:str = get_env_file()
        

    