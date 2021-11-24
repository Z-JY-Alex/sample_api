#coding:utf-8
from fastapi import APIRouter, Body
from app.project_2.code.code_4 import compare_text_len
from app.project_2.schema import *
example = {
    'text1': "this is a test3.",
    'text2': "this is.",
}

router = APIRouter()

@router.post('/test4', summary='test4',tags=['project2'])
def text_vector(test4:test4=Body(...,example=example)):
    text1, text2 = test4.text1, test4.text2
    res = compare_text_len(text1, text2)
    return {
        "res": res,
        "message": "OK",
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api_4:router", host="127.0.0.1", port=5000, log_level="info")