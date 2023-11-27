from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from src.infrastructure.configs.enviroment import get_enviroment_settinngs

env = get_enviroment_settinngs()
    
DATABASE_URL = f"{env().DATABASE_ENGINE}://{env().DATABASE_USER}:{env().DATABASE_PASSWORD}@{env().DATABASE_HOST}:{env().DATABASE_PORT}/{env().DATABASE_NAME}"
    
engine = create_engine(DATABASE_URL,echo=True, pool_size=20, max_overflow=30)

SessionLocal =sessionmaker(autocommit=False, autoflush=False,bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    
    db = SessionLocal()
    
    try:
    
        yield db
    
    finally:
    
        db.close()