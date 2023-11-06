from src.infrastructure.schemas.user_schema import UserSchema
from src.services.user_service import UserService
from src.domain.models.user_entity import UserEntity as User

class FindByEmailUserUseCase:
    
    def __init__(self) -> None:
        
        self.user_service = UserService()
        
    def execute(self,user:User) -> User:
        
        try:
            
            return self.user_service.find_by_email(user)
        
        except Exception as error:
        
            raise error