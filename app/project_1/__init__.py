from . import api_1, api_2
from fastapi import APIRouter

project_1_router = APIRouter()
project_1_router.include_router(api_1.router, prefix='/project_1')
project_1_router.include_router(api_2.router, prefix='/project_1')

