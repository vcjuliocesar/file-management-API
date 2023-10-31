import pytest
from src.domain.models.user_entity import UserEntity
from src.domain.exceptions.user_already_exists_exception import UserAlreadyExistsException
from src.domain.exceptions.user_not_found_exception import UserNotFoundException
from src.infrastructure.schemas.user_schema import UserSchema
from src.services.user_service import UserService

class TestUserService():
    
    @pytest.fixture
    def user_service(self):
        
        return UserService()
    
    @pytest.fixture
    def create_user(self):
        
        return UserSchema(
            name="Jhon Doe",
            email="jhon.doe@example.com",
            password="MySr3cr3tP4ssw0rd_123",
            is_active=True,
            is_admin=False
        )
    
    def test_it_retun_an_exception_if_user_already_exists(self,user_service,create_user):
        
        user_entity = user_service.create(create_user)
        
        with pytest.raises(UserAlreadyExistsException):
            
            new_user_schema = UserSchema(
                name="Jhon Doe",
                email="jhon.doe@example.com",
                password="MySr3cr3tP4ssw0rd_123",
                is_active=True,
                is_admin=False
            )
        
            user_service.create(new_user_schema)
            
        user_service.delete(user_entity.id)
        
    def test_it_return_an_exception_is_user_not_exists(self,user_service):
        
        with pytest.raises(UserNotFoundException):
            
            user_service.update(1,UserEntity())
    
    def test_it_can_create_user(self,user_service,create_user):
        
        user_entity = user_service.create(create_user)
        
        assert isinstance(user_entity,UserEntity)
        assert user_entity.name == "Jhon Doe"
        assert user_entity.email == "jhon.doe@example.com"
        
        user_service.delete(user_entity.id)
    
    def test_it_retun_all_users(self,user_service,create_user):
        
        user_entity = user_service.create(create_user)
        
        users = user_service.get_all()
        
        assert isinstance(users,list)
        
        user_service.delete(user_entity.id)
    
    def test_it_can_find_user_by_id(self,user_service,create_user):
         
        user_entity = user_service.create(create_user)
        
        user = user_service.find_by_id(user_entity.id)
        
        assert user.name == "Jhon Doe"
        assert user.email == "jhon.doe@example.com"
        
        user_service.delete(user_entity.id)
    
    def test_it_find_a_user_by_criteria_and_return_one_result(self,user_service,create_user):
         
        user_schema2 = UserSchema(
            name="Jhanne Doe",
            email="jhanne.doe@example.com",
            password="MySr3cr3tP4ssw0rd_123",
            is_active=True,
            is_admin=False
        )
        
        user_entity1 = user_service.create(create_user)

        user_entity2 = user_service.create(user_schema2)

        user = user_service.find_one({"name":"Jhon Doe","email":"jhon.doe@example.com"})
        
        assert user.name == "Jhon Doe"
        
        assert user.email == "jhon.doe@example.com"
        
        user_service.delete(user_entity1.id)
        
        user_service.delete(user_entity2.id)
    
    def test_it_can_update_user(self,user_service,create_user):
         
        user_entity = user_service.create(create_user)
        
        user = user_service.find_by_id(user_entity.id)
        
        user.name = "Jhane Doe"
        user.email = "new.jhane.doe@example.com"
        user.password = create_user.password
        user.is_active = False
        user.is_admin = create_user.is_admin
        
        new_user = user_service.update(user.id,user)
        
        assert new_user.name == "Jhane Doe"
        assert new_user.email == "new.jhane.doe@example.com"
        assert not new_user.is_active
        
        user_service.delete(new_user.id)
        