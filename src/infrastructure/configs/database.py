import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from src.infrastructure.configs.enviroment import get_enviroment_settinngs

env = get_enviroment_settinngs()

'''
main database
'''    
DATABASE_URL = f"{env().DATABASE_ENGINE}://{env().DATABASE_USER}:{env().DATABASE_PASSWORD}@{env().DATABASE_HOST}:{env().DATABASE_PORT}/{env().DATABASE_NAME}"

'''
local database
'''
#sqlite_db_path = os.path.join(os.path.dirname(__file__), 'local_database.sqlite')
#engine = create_engine(f'sqlite:///{sqlite_db_path}', echo=True)   

engine = create_engine(DATABASE_URL,echo=True)

Session =sessionmaker(bind=engine)

Base = declarative_base()