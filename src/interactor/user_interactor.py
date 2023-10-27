from src.infrastructure.repositories.user_repository import UserRepository
from src.domain.models.user_entity import UserEntity as User
from src.infrastructure.schemas.user_schema import UserSchema

class UserInteractor:
    
    def __init__(self) -> None:
        
        self.user_repository = UserRepository()
         
    def create(self,user:UserSchema) -> User:
        
        return self.user_repository.create(User(**user.dict()))