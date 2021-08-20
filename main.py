from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/blog')
def index(limit=10,published:bool=True,sort:Optional[str]=None):
    if published:
        return {'data':f'{limit} published blog list'}
    else:
        return {'data':f'{limit} blog list'}

@app.get('/blog/{id}')
def blog(id):
    return {'data':id}  


class Blog(BaseModel):
    title:str
    body:str
    published_at:Optional[bool]

@app.post('/blog')
def create_blog(request:Blog):
    return {'data':f'create blog {request.title}'} 


if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=9000)         