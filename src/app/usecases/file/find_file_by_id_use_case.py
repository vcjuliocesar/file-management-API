from fastapi import Depends
from src.services.file_service import FileService
from src.domain.models.file_entity import FileEntity
class FindFileByIdUseCase:
    
    def __init__(self,file_service:FileService = Depends()) -> None:
        
        self.file_service = file_service
        
    def execute(self,file_id:int,token) -> FileEntity:
        
        try:
            
            return self.file_service.find_by_id(file_id,token)
            
        except Exception as error:
            
            raise error