from fastapi import Depends
from src.domain.models.file_entity import FileEntity
from src.services.file_service import FileService
class GetAllFilesUseCase:
    
    def __init__(self,file_service:FileService = Depends()) -> None:
        
        self.file_service = file_service
        
    def execute(self,owner:int) -> FileEntity:
        
        try:
            
            return self.file_service.get_all(owner)
        
        except Exception as error:
            
            raise error