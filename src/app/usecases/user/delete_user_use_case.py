from fastapi import Depends
from src.services.user_service import UserService
from src.domain.models.user_entity import UserEntity as User

class DeleteUserUseCase:
    
    def __init__(self,user_service:UserService = Depends()) -> None:
        
        self.user_service = user_service
        
    def execute(self,user_id:int) -> None:
        
        try:
        
            return self.user_service.delete(user_id)
        
        except Exception as error:
            
            raise error