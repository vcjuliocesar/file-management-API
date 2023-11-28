from fastapi import Depends
from src.infrastructure.schemas.file_schema import FilePostRequest
from src.services.file_service import FileService
from src.domain.models.file_entity import FileEntity as File

class CreateFileUseCase:
    
    def __init__(self,file_service:FileService = Depends()) -> None:
        
        self.file_service = file_service
        
    def execute(self,name:str,description:str,file,token:str) -> File:
        
        try:
            
            return self.file_service.create(name,description,file,token)
        
        except Exception as error:
        
            raise error