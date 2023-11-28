from fastapi import Depends
from src.services.file_service import FileService

class DeleteFileUseCase:
    
    def __init__(self,file_service:FileService = Depends()) -> None:
        
        self.file_service = file_service
        
    def execute(self,id:int,token) -> None:
        
        try:
            
            return self.file_service.delete(id,token)
        
        except Exception as error:
        
            raise error