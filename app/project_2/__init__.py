from . import api_3, api_4
from fastapi import APIRouter

project_2_router = APIRouter()
project_2_router.include_router(api_3.router, prefix='/project_2')
project_2_router.include_router(api_4.router, prefix='/project_2')

