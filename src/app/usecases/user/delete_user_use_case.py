from src.interactor.user_interactor import UserInteractor
from src.domain.models.user_entity import UserEntity as User

class DeleteUserUseCase:
    
    def __init__(self) -> None:
        
        self.user_interactor = UserInteractor()
        
    def execute(self,user_id:int) -> None:
        
        try:
        
            return self.user_interactor.delete(user_id)
        
        except Exception as error:
            
            raise error