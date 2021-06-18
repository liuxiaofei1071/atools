# _*_ coding:utf-8 _*_
# @Time:2020/11/2 12:48
# @Author:Cadman
# @File middle.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from apps.config import settings
from .logs import logger as log


def init_middlewares(app: FastAPI):
    """初始化中间件"""
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
        allow_methods=settings.CORS_ALLOW_METHODS,
        allow_headers=settings.CORS_ALLOW_HEADERS,
    )

class CustomMiddleware(BaseHTTPMiddleware):
    """自定义中间件-http 记录"""
    async def dispatch(self, request, call_next):
        http_request = request.scope
        print(http_request)
        print(type(http_request))
        response = await call_next(request)
        code = response.status_code
        protocol_type = http_request.get('type').upper()
        asgi_ver = http_request.get('asgi').get("version")
        http_ver = http_request.get('http_version')

        client_ip,client_port = http_request.get("client")
        method = http_request.get("method")
        api_path = http_request.get("path")

        log.info(f'{client_ip}:{client_port} - "{method} {api_path} {protocol_type}/{http_ver} ASGI/{asgi_ver} " {code}')
        response.headers['Custom-Header'] = 'Example next'
        return response