from src.infrastructure.schemas.user_schema import UserPostRequest
from src.services.user_service import UserService
from src.domain.models.user_entity import UserEntity as User
from fastapi import Depends

class CreateUserUseCase:
    
    def __init__(self,user_service:UserService = Depends()) -> None:
        
        self.user_service = user_service
        
    def execute(self,user_data:UserPostRequest) -> User:
        
        try:
            
            return self.user_service.create(user_data)
        
        except Exception as error:
        
            raise error