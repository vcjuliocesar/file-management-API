class FileAlreadyExistsException(Exception):
    
    def __init__(self, message:str = "File already exists") -> None:
        
        self.message = message
        
        super().__init__(self.message)