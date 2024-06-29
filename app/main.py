from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory='template')

@app.get('/')
def index(request:Request):
    return templates.TemplateResponse(request=request, name='index.html')










if __name__ == '__main__':
    uvicorn.run('main:app', 
                port = 8000, 
                host='127.0.0.1', 
                reload=True)
    




