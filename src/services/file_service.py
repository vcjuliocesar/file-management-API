from src.domain.models.file_entity import FileEntity as File
from src.domain.exceptions.user_already_exists_exception import UserAlreadyExistsException
from src.domain.exceptions.user_not_found_exception import UserNotFoundException
from src.domain.exceptions.file_already_exists_exception import FileAlreadyExistsException
from src.domain.exceptions.file_not_found_exception import FileNotFoundException
from src.infrastructure.repositories.file_repository import FileRepository
from src.infrastructure.schemas.file_schema import FileSchema

class FileService:
    
    def __init__(self) -> None:
        
        self.file_repository = FileRepository()
    
    def get_all(self) -> list:
        
        return self.file_repository.get()
    
    def find_by_id(self,file_id:int):
        
        return self.file_repository.find_by_id(file_id)
 
    def find_one(self,criteria:dict) -> list:
        
        return self.file_repository.find_one(criteria)
        
    def create(self,file:FileSchema) -> File:
        
        exist = self.file_repository.find_one({"name":file.name})
        
        if exist:
            
            raise FileAlreadyExistsException()
        
        return self.file_repository.create(File(**file.model_dump()))
    
    def update(self,file_id:int,file_data:FileSchema) -> File:
        pass
        # user = self.file_repository.find_by_id(file_id)
        
        # if not user:
            
        #      raise FileNotFoundException()
        
        # f
        
        # return self.file_repository.update(file)
    
    def delete(self,file_id:int) -> None:
        
        file = self.find_by_id(file_id)
        
        if not file:
            
            raise FileNotFoundException()
         
        return self.file_repository.delete(file)