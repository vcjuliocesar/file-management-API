# import os

# UPLOAD_DIR = "uploads"

# os.makedirs(UPLOAD_DIR,exist_ok=True)

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif', 'xlsx', 'xls', 'doc', 'docx', 'pdf'}

def allowed_file(filename:str):
    
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

def new_filename(name:str,filename):
    
    file_extension = filename.rsplit('.',1)[1].lower()
    
    return f"{name}.{file_extension}"