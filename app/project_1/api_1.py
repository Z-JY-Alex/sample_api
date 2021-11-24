#coding:utf-8

from fastapi import APIRouter, Body
from app.project_1.code.code_1 import text_msg
from app.project_1.schema import *
example = {
    'text': "this is a test.",
}

router = APIRouter()

@router.post('/test1', summary='test1',tags=['project1'])
def text_vector(text1:test1=Body(...,example=example)):
    text = text1.text
    res = text_msg(text)
    return {
        "res": res,
        "message": "OK",
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api_1:router", host="127.0.0.1", port=5000, log_level="info")