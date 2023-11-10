from urllib.parse import urlparse
from fastapi import Request,APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

index_router = APIRouter()

templates = Jinja2Templates(directory="./src/app/templates")

@index_router.get("/", response_class=HTMLResponse)
async def read_root(request:Request):
    
    url_parse = urlparse(str(request.url))
    
    client_host = url_parse.hostname
    
    client_port = url_parse.port
    
    template_vars = {"host":client_host,"port":client_port}
    
    return templates.TemplateResponse("index.html", {"request": request,**template_vars})