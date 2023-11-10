from fastapi import FastAPI,Request,HTTPException
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="./src/app/templates")

@app.exception_handler(HTTPException)
async def not_found_exception_handler(request: Request, exc: HTTPException):
    
    return templates.TemplateResponse("404.html", {"request": request}, status_code=404)