from src.services.file_service import FileService
from src.domain.models.file_entity import FileEntity
class FindFileByIdUseCase:
    
    def __init__(self) -> None:
        
        self.file_service = FileService()
        
    def execute(self,file_id:int,token) -> FileEntity:
        
        try:
            
            return self.file_service.find_by_id(file_id,token)
            
        except Exception as error:
            
            raise error