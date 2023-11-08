class FileNoAllowedException(Exception):
    
    def __init__(self, message:str = "File no allowed") -> None:
        
        self.message = message
        
        super().__init__(self.message)