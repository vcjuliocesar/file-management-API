import unittest
from httpx import AsyncClient
from fastapi.testclient import TestClient
from src.app.main import app 

class TestUserRoutes(unittest.TestCase):
    
    def setUp(self) -> None:
        self.client = TestClient(app)
        
    async def test_it_can_created_a_user(self):
        pass
        # user_data = {
        #      "name":"Jhon Doe",
        #      "email":"jhon.doe@example.com",
        #      "password":"MySr3cr3tP4ssw0rd_123",
        # }
        
        # response = await self.client.post("/api/v1/users",json=user_data)
        # #print(response)
        # self.assertEqual(response.status_code,200)
        
        


if __name__ == "__main__":
    
    unittest.main()