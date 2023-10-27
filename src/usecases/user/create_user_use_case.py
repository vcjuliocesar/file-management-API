from src.infrastructure.schemas.user_schema import UserPostRequest
from src.interactor.user_interactor import UserInteractor
from src.domain.models.user_entity import UserEntity as User

class CreateUserUseCase:
    
    def __init__(self) -> None:
        
        self.user_interactor = UserInteractor()
        
    def execute(self,user_data:UserPostRequest) -> User:
        
        try:
            
            return self.user_interactor.create(user_data)
        
        except Exception as error:
        
            raise error