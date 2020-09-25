# -*- coding: utf-8 -*-
# @Time : 2020/9/21 12:08
# @Author : Cassie Daddy
# @Email : liuxiaofeikeke@163.com
# @Site : 
# @File : start.py


from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from apps.controller import router

def create_app():
    app = FastAPI()

    origins = [
        "http://localhost.tiangolo.com",
        "https://localhost.tiangolo.com",
        "http://localhost",
        "http://localhost:8080",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(router,prefix="/api/v1")
    return app


