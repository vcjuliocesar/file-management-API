class FileNotFoundException(Exception):
    
    def __init__(self, message:str = "File not found") -> None:
        
        self.message = message
        
        super().__init__(self.message)