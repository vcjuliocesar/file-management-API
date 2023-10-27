from src.infrastructure.schemas.user_schema import UserSchema
from src.interactor.user_interactor import UserInteractor
from src.domain.models.user_entity import UserEntity as User

class UpdateUserUseCase:
    
    def __init__(self) -> None:
        
        self.user_interactor = UserInteractor()
        
    def execute(self,user_id:int,user_data:UserSchema) -> User:
        
        try:
            
            return self.user_interactor.update(user_id,user_data)
        
        except Exception as error:
        
            raise error