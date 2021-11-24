#coding:utf-8

from fastapi import FastAPI
from app.project_1 import project_1_router
from app.project_2 import project_2_router

app = FastAPI(
    title="api模板接口",
    version="0.1",
    description="",
)

app.include_router(project_1_router, tags=[""])
app.include_router(project_2_router, tags=[""])