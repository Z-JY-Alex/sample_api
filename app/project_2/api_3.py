#coding:utf-8
from fastapi import APIRouter, Body
from app.project_2.code.code_3 import text_len
from app.project_2.schema import *
example = {
    'text': "this is a test2.",
}

router = APIRouter()

@router.post('/test3', summary='test3',tags=['project2'])
def text_vector(test3:test3=Body(...,example=example)):
    text = test3.text
    res = text_len(text)
    return {
        "res": res,
        "message": "OK",
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api_3:router", host="127.0.0.1", port=5000, log_level="info")