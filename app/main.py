from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn
from src.db import session_titan
from fastapi.responses import Response

app = FastAPI()
templates = Jinja2Templates(directory='template')

@app.get('/')
def index(request:Request):
    return templates.TemplateResponse(request=request, name='index.html')

@app.get('/list')
def get_list(request: Request):
    return templates.TemplateResponse(request=request, name='list.html')

@app.get('/list_bay/')
def list(request: Request):
    database = session_titan.get_table_data('readyMadeSolutions')
    name_data = []
    
    for i in database:
        

        name_data.append({"name":i[1]})
    
    print(name_data)
        
            
    return Response(content=name_data)














if __name__ == '__main__':
    uvicorn.run('main:app', 
                port = 8000, 
                host='127.0.0.1', 
                reload=True)
    




