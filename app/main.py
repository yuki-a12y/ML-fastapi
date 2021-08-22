from fastapi import FastAPI
from fastapi import Query, Path
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()


@app.get('/') # methodとendpointの指定
async def hello():
    return {"text": "hello world!"} 
