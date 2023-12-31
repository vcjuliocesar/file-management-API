from fastapi import Depends
from src.infrastructure.schemas.user_schema import UserSchema,UserPostRequest
from src.services.user_service import UserService
from src.domain.models.user_entity import UserEntity as User

class UpdateUserUseCase:
    
    def __init__(self,user_service:UserService = Depends()) -> None:
        
        self.user_service = user_service
        
    def execute(self,user_id:int,user_data:UserSchema) -> User:
        
        try:
            
            return self.user_service.update(user_id,user_data)
        
        except Exception as error:
        
            raise error