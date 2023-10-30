import unittest
from src.domain.models.user_entity import UserEntity
from src.domain.exceptions.user_already_exists_exception import UserAlreadyExistsException
from src.domain.exceptions.user_not_found_exception import UserNotFoundException
from src.infrastructure.schemas.user_schema import UserSchema
from src.services.user_service import UserService

class TestUserService(unittest.TestCase):
    
    def test_it_retun_an_exception_if_user_already_exists(self):
        
        user_service = UserService()
        
        user_schema = UserSchema(
            name="Jhon Doe",
            email="jhon.doe@example.com",
            password="MySr3cr3tP4ssw0rd_123",
            is_active=True,
            is_admin=False
        )
        
        user_entity = user_service.create(user_schema)
        
        with self.assertRaises(UserAlreadyExistsException):
            
            new_user_schema = UserSchema(
                name="Jhon Doe",
                email="jhon.doe@example.com",
                password="MySr3cr3tP4ssw0rd_123",
                is_active=True,
                is_admin=False
            )
        
            user_service.create(new_user_schema)
            
        user_service.delete(user_entity.id)
        
    def test_it_return_an_exception_is_user_not_exists(self):
         
        user_service = UserService()
        
        with self.assertRaises(UserNotFoundException):
            
            user_service.update(1,UserEntity())
    
    def test_it_can_create_user(self):
        
        user_service = UserService() 
        
        user_schema = UserSchema(
            name="Jhon Doe",
            email="jhon.doe@example.com",
            password="MySr3cr3tP4ssw0rd_123",
            is_active=True,
            is_admin=False
        )
        
        user_entity = user_service.create(user_schema)
        
        self.assertTrue(isinstance(user_entity,UserEntity))
        self.assertEqual("Jhon Doe",user_entity.name)
        self.assertEqual("jhon.doe@example.com",user_entity.email)
        
        user_service.delete(user_entity.id)
    
    def test_it_retun_all_users(self):
        
        user_service = UserService() 
        
        user_schema = UserSchema(
            name="Jhon Doe",
            email="jhon.doe@example.com",
            password="MySr3cr3tP4ssw0rd_123",
            is_active=True,
            is_admin=False
        )
        
        user_entity = user_service.create(user_schema)
        
        users = user_service.get_all()
        
        self.assertTrue(isinstance(users,list))
        
        user_service.delete(user_entity.id)
    
    def test_it_can_find_user_by_id(self):
        
        user_service = UserService() 
        
        user_schema = UserSchema(
            name="Jhon Doe",
            email="jhon.doe@example.com",
            password="MySr3cr3tP4ssw0rd_123",
            is_active=True,
            is_admin=False
        )
        
        user_entity = user_service.create(user_schema)
        
        user = user_service.find_by_id(user_entity.id)
        
        self.assertEqual("Jhon Doe",user.name)
        self.assertEqual("jhon.doe@example.com",user.email)
        
        user_service.delete(user_entity.id)
    
    def test_it_find_a_user_by_criteria_and_return_one_result(self):
        
        user_service = UserService()
        
        user_schema1 = UserSchema(
            name="Jhon Doe",
            email="jhon.doe@example.com",
            password="MySr3cr3tP4ssw0rd_123",
            is_active=True,
            is_admin=False
        )
        
        user_schema2 = UserSchema(
            name="Jhanne Doe",
            email="jhanne.doe@example.com",
            password="MySr3cr3tP4ssw0rd_123",
            is_active=True,
            is_admin=False
        )
        
        user_entity1 = user_service.create(user_schema1)

        user_entity2 = user_service.create(user_schema2)

        user = user_service.find_one({"name":"Jhon Doe","email":"jhon.doe@example.com"})
        
        self.assertEqual("Jhon Doe",user.name)
        
        self.assertEqual("jhon.doe@example.com",user.email)
        
        user_service.delete(user_entity1.id)
        
        user_service.delete(user_entity2.id)
    
    def test_it_can_update_user(self):
        
        user_service = UserService() 
        
        user_schema = UserSchema(
            name="Jhon Doe",
            email="jhon.doe@example.com",
            password="MySr3cr3tP4ssw0rd_123",
            is_active=True,
            is_admin=False
        )
        
        user_entity = user_service.create(user_schema)
        
        user = user_service.find_by_id(user_entity.id)
        
        user.name = "Jhane Doe"
        user.email = "new.jhane.doe@example.com"
        user.password = user_schema.password
        user.is_active = False
        user.is_admin = user_schema.is_admin
        
        new_user = user_service.update(user.id,user)
        
        self.assertEqual("Jhane Doe",new_user.name)
        self.assertEqual("new.jhane.doe@example.com",new_user.email)
        self.assertFalse(new_user.is_active)
        
        user_service.delete(new_user.id)
        
if __name__ == "__main__" :
    
    unittest.main()