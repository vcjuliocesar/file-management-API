from fastapi import Depends
from src.infrastructure.schemas.user_schema import UserSchema
from src.services.user_service import UserService
from src.domain.models.user_entity import UserEntity as User

class FindByEmailUserUseCase:
    
    def __init__(self,user_service:UserService = Depends()) -> None:
        
        self.user_service = user_service
        
    def execute(self,user:User) -> User:
        
        try:
            
            return self.user_service.find_by_email(user)
        
        except Exception as error:
        
            raise error