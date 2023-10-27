from src.infrastructure.repositories.user_repository import UserRepository
from src.domain.models.user_entity import UserEntity as User
from src.infrastructure.schemas.user_schema import UserSchema

class UserInteractor:
    
    def __init__(self) -> None:
        
        self.user_repository = UserRepository()
    
    def find_by_id(self,user_id:int):
        
        return self.user_repository.find_by_id(user_id)
        
    def create(self,user:UserSchema) -> User:
        
        return self.user_repository.create(User(**user.dict()))
    
    def update(self,user:User) -> User:
        
        return self.user_repository.update(user)
    
    def delete(self,user:User) -> None:
        
        return self.user_repository.delete(user)