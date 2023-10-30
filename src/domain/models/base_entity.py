from src.infrastructure.configs.database import Base,engine

EntityBase = Base

def init():
    EntityBase.metadata.create_all(bind=engine)