#coding:utf-8

import uvicorn
from app.main import app
import os

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=os.getenv("PORT", 5000), log_level="info")
