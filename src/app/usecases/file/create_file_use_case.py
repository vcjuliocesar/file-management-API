from src.infrastructure.schemas.file_schema import FilePostRequest
from src.services.file_service import FileService
from src.domain.models.file_entity import FileEntity as File

class CreateFileUseCase:
    
    def __init__(self) -> None:
        
        self.file_service = FileService()
        
    def execute(self,file_data:FilePostRequest,token) -> File:
        
        try:
            
            return self.file_service.create(file_data)
        
        except Exception as error:
        
            raise error