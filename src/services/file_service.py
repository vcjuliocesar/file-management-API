import os
from src.domain.models.file_entity import FileEntity as File
from src.domain.exceptions.user_already_exists_exception import UserAlreadyExistsException
from src.domain.exceptions.user_not_found_exception import UserNotFoundException
from src.domain.exceptions.file_already_exists_exception import FileAlreadyExistsException
from src.domain.exceptions.file_not_found_exception import FileNotFoundException
from src.domain.exceptions.file_no_allowed_exception import FileNoAllowedException
from src.infrastructure.repositories.file_repository import FileRepository
from src.infrastructure.schemas.file_schema import FileSchema
from src.infrastructure.validations.file_validation import *

class FileService:
    
    def __init__(self) -> None:
        
        self.file_repository = FileRepository()
    
    def get_all(self) -> list:
        
        return self.file_repository.get()
    
    def find_by_id(self,file_id:int):
        
        return self.file_repository.find_by_id(file_id)
 
    def find_one(self,criteria:dict) -> list:
        
        return self.file_repository.find_one(criteria)
        
    def create(self,name,description,file,token) -> File:
        
        file_schema = FileSchema(
            name=name,
            path=file.filename,
            description=description,
            owner_id=token.id)
        
        exist = self.file_repository.find_one({"name":file_schema.name})
        
        if exist:
            
            raise FileAlreadyExistsException()
        
        if not allowed_file(file_schema.path):
            
           raise FileNoAllowedException()
        
        new_file_name = new_filename(file_schema.name,file_schema.path)
        
        UPLOAD_DIR = "uploads"
        
        USER_DIR = token.name.replace(" ","_").lower()
        
        os.makedirs(os.path.join(UPLOAD_DIR,USER_DIR),exist_ok=True)
        
        file_path = os.path.join(UPLOAD_DIR,USER_DIR,new_file_name)
        
        with open(file_path,"wb") as uploaded_file:
            
            uploaded_file.write(file.file.read())
        
        file_schema.path = file_path
        
        return self.file_repository.create(File(**file_schema.model_dump()))
    
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