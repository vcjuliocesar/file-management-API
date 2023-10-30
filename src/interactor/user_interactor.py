from src.infrastructure.repositories.user_repository import UserRepository
from src.domain.models.user_entity import UserEntity as User
from src.infrastructure.schemas.user_schema import UserSchema

class UserInteractor:
    
    def __init__(self) -> None:
        
        self.user_repository = UserRepository()
    
    def get_all(self) -> list:
        
        return self.user_repository.get()
    
    def find_by_id(self,user_id:int):
        
        return self.user_repository.find_by_id(user_id)
    
    def find_one(self,criteria:dict) -> list:
        
        return self.user_repository.find_one(criteria)
        
    def create(self,user:UserSchema) -> User:
        
        return self.user_repository.create(User(**user.dict()))
    
    def update(self,user_id:int,user_data:UserSchema) -> User:
        
        user = self.user_repository.find_by_id(user_id)
        
        user.name = user_data.name
        
        user.email = user_data.email
        
        user.password = user_data.password
        
        user.is_active = user_data.is_active
        
        user.is_admin = user_data.is_admin
        
        return self.user_repository.update(user)
    
    def delete(self,user_id:int) -> None:
        
        user = self.find_by_id(user_id)
        
        return self.user_repository.delete(user)