from fastapi import FastAPI
from fastapi import Query, Path
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()


@app.get('/') # methodとendpointの指定
async def hello():
    return {"text": "hello world!"} 

@app.get('/get/{path}')
async def path_and_query_params(
        path: str, 
        query: int, 
        default_none: Optional[str] = None):
    return {"text": f"hello, {path}, {query} and {default_none}"}

@app.get('/validation/{path}')
async def validation(
        string: str = Query(None, min_length=2, max_length=5, regex=r'[a-c]+.'),
        integer: int = Query(..., gt=1, le=3),  # required
        alias_query: str = Query('default', alias='alias-query'),
        path: int = Path(10)):

    return {"string": string, "integer": integer, "alias-query": alias_query, "path": path}

class Data(BaseModel):
    """request data用の型ヒントがされたクラス"""
    string: str
    default_none: Optional[int] = None
    lists: List[int]

@app.post('/post')
async def declare_request_body(data: Data):
    return {"text": f"hello, {data.string}, {data.default_none}, {data.lists}"}
