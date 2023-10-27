from src.infrastructure.schemas.user_schema import UserSchema
from src.interactor.user_interactor import UserInteractor
from src.domain.models.user_entity import UserEntity as User

class FindByIdUserUseCase:
    
    def __init__(self) -> None:
        
        self.user_interactor = UserInteractor()
        
    def execute(self,user_id:int) -> User:
        
        try:
            
            return self.user_interactor.find_by_id(user_id)
        
        except Exception as error:
        
            raise error