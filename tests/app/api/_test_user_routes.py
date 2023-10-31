import os
import pytest
from httpx import AsyncClient
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from src.app.main import app

#WIP
class TestUserRoutes():
    
    @pytest.fixture(scope="module")
    def setup_database():
        
        sqlite_File_name = "./database_dev.sqlite"

        DATABASE_URL = f"sqlite:///{os.path.join(os.path.dirname(os.path.realpath(__file__)),sqlite_File_name)}"
        
        engine = create_engine(DATABASE_URL,echo=True)

        Session =sessionmaker(bind=engine)
        
        Base = declarative_base()
        
        Base.metadata.create_all(bind=engine)
        
        yield Session
        
        Base.metadata.drop_all(bind=engine)

        
     
    @pytest.mark.asyncio    
    async def test_it_can_created_a_user(setup_database):
          
        user_data = {
             "name":"Jhon Doe",
             "email":"jhon.doe@example.com",
             "password":"MySr3cr3tP4ssw0rd_123",
        }
        
        async with AsyncClient(app=app,base_url="http://127.0.0.1:8000") as client:
            response = await client.post("/api/v1/users",json=user_data)
        
        assert response.status_code == 200
        
        user = response.json()
        
        assert user["name"] == "Jhon Doe"