#coding:utf-8
from fastapi import APIRouter, Body
from app.project_1.code.code_2 import text_len
from app.project_1.schema import *
examples = {
    "eg1":{
        "summary": "例子一",
        "description": "例子一",
        "value":{
            "text":'test1',
            "k": 3,
        }
            },
    "eg2":{
        "summary": "例子2",
        "description": "test2",
        "value":{
            "text":'test2',
            "k": 3,
                }
            },
}

router = APIRouter()

@router.post('/test2', summary='test2',tags=['project1'])
def text_vector(text2:test2=Body(...,examples=examples)):
    text, k = text2.text, text2.k
    res = text_len(text, k)
    return {
        "res": res,
        "message": "OK",
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api_2:router", host="127.0.0.1", port=5000, log_level="info")