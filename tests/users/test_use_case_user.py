import unittest
from fastapi.testclient import TestClient
from src.app.main import app

client = TestClient(app)

class TestUseCaseUser(unittest.TestCase):
    
    def test_it_can_create_user(self) -> None:
        user_data = {
            
        }
        
        response = client.post('/user')       