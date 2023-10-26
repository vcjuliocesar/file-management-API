import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from src.infrastructure.configs.enviroment import get_enviroment

env = get_enviroment()

if env.Config.env_file != "PRODUCTION":
    
    sqlite_File_name = "./database_dev.sqlite"

    DATABASE_URL = f"sqlite:///{os.path.join(os.path.dirname(os.path.realpath(__file__)),sqlite_File_name)}"

else:
    
     DATABASE_URL = f"{env.DATABASE_ENGINE}://{env.DATABASE_USER}:{env.DATABASE_PASSWORD}@{env.DATABASE_HOST}/{env.DATABASE_NAME}"
    
engine = create_engine(DATABASE_URL,echo=True)

Session =sessionmaker(bind=engine)

Base = declarative_base()