# _*_ coding:utf-8 _*_
# @Time:2020/11/2 12:48
# @Author:Cadman
# @File middle.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from apps.config import settings


def init_middlewares(app: FastAPI):
    """初始化中间件"""
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
        allow_methods=settings.CORS_ALLOW_METHODS,
        allow_headers=settings.CORS_ALLOW_HEADERS,
    )
