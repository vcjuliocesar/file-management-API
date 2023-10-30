from src.infrastructure.schemas.user_schema import UserSchema
from src.services.user_service import UserService
from src.domain.models.user_entity import UserEntity as User

class GetAllUsersUseCase:
    
    def __init__(self) -> None:
        
        self.user_interactor = UserService()
        
    def execute(self) -> list:
        
        try:
            
            return self.user_interactor.get_all()
        
        except Exception as error:
        
            raise error