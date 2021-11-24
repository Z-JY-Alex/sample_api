from pydantic import BaseModel

class test1(BaseModel):
    text: str

class test2(BaseModel):
    text: str
    k: int
