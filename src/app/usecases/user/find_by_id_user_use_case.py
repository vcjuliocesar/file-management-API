from fastapi import Depends
from src.infrastructure.schemas.user_schema import UserSchema
from src.services.user_service import UserService
from src.domain.models.user_entity import UserEntity as User

class FindByIdUserUseCase:
    
    def __init__(self,user_service:UserService = Depends()) -> None:
        
        self.user_service = user_service
        
    def execute(self,user_id:int) -> User:
        
        try:
            
            return self.user_service.find_by_id(user_id)
        
        except Exception as error:
        
            raise error