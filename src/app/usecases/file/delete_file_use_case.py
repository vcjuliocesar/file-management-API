from src.services.file_service import FileService

class DeleteFileUseCase:
    
    def __init__(self) -> None:
        
        self.file_service = FileService()
        
    def execute(self,id:int,token) -> None:
        
        try:
            
            return self.file_service.delete(id,token)
        
        except Exception as error:
        
            raise error