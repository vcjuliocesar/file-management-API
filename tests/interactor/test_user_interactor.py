import unittest
from src.domain.models.user_entity import UserEntity
from src.infrastructure.schemas.user_schema import UserSchema,UserPostRequest
from src.interactor.user_interactor import UserInteractor

class TestUserInteractor(unittest.TestCase):
    
    def test_it_can_create_user(self):
        
        user_interactor = UserInteractor() 
        
        user_schema = UserSchema(
            name="Jhon Doe",
            email="jhon.doe@example.com",
            password="MySr3cr3tP4ssw0rd_123",
            is_active=True,
            is_admin=False
        )
        
        user_entity = user_interactor.create(user_schema)
        
        self.assertTrue(isinstance(user_entity,UserEntity))
        self.assertEqual("Jhon Doe",user_entity.name)
        self.assertEqual("jhon.doe@example.com",user_entity.email)
        
        user_interactor.delete(user_entity.id)
    
    def test_it_retun_all_users(self):
        
        user_interactor = UserInteractor() 
        
        user_schema = UserSchema(
            name="Jhon Doe",
            email="jhon.doe@example.com",
            password="MySr3cr3tP4ssw0rd_123",
            is_active=True,
            is_admin=False
        )
        
        user_entity = user_interactor.create(user_schema)
        
        users = user_interactor.get_all()
        
        self.assertTrue(isinstance(users,list))
        
        user_interactor.delete(user_entity.id)
    
    def test_it_can_find_user_by_id(self):
        
        user_interactor = UserInteractor() 
        
        user_schema = UserSchema(
            name="Jhon Doe",
            email="jhon.doe@example.com",
            password="MySr3cr3tP4ssw0rd_123",
            is_active=True,
            is_admin=False
        )
        
        user_entity = user_interactor.create(user_schema)
        
        user = user_interactor.find_by_id(user_entity.id)
        
        self.assertEqual("Jhon Doe",user.name)
        self.assertEqual("jhon.doe@example.com",user.email)
        
        user_interactor.delete(user_entity.id)
    
    def test_it_find_a_user_by_criteria_and_return_one_result(self):
        
        user_interactor = UserInteractor()
        
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
        
        user_entity1 = user_interactor.create(user_schema1)

        user_entity2 = user_interactor.create(user_schema2)

        user = user_interactor.find_one({"name":"Jhon Doe","email":"jhon.doe@example.com"})
        
        self.assertEqual("Jhon Doe",user.name)
        
        self.assertEqual("jhon.doe@example.com",user.email)
        
        user_interactor.delete(user_entity1.id)
        
        user_interactor.delete(user_entity2.id)
    
    def test_it_can_update_user(self):
        
        user_interactor = UserInteractor() 
        
        user_schema = UserSchema(
            name="Jhon Doe",
            email="jhon.doe@example.com",
            password="MySr3cr3tP4ssw0rd_123",
            is_active=True,
            is_admin=False
        )
        
        user_entity = user_interactor.create(user_schema)
        
        user = user_interactor.find_by_id(user_entity.id)
        
        user.name = "Jhane Doe"
        user.email = "new.jhane.doe@example.com"
        user.password = user_schema.password
        user.is_active = False
        user.is_admin = user_schema.is_admin
        
        new_user = user_interactor.update(user.id,user)
        
        self.assertEqual("Jhane Doe",new_user.name)
        self.assertEqual("new.jhane.doe@example.com",new_user.email)
        self.assertFalse(new_user.is_active)
        
        user_interactor.delete(new_user.id)
        
if __name__ == "__main__" :
    
    unittest.main()