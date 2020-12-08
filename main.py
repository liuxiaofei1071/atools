# -*- coding: utf-8 -*-
# @Time : 2020/9/21 12:08
# @Author : Cadman
# @Email : liuxiaofeikeke@163.com
# @Site : 
# @File : main.py

"""
项目入口
"""

from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError

from apps.core.base_response import UnicornException
from apps.core.error.http_error import http_error_handler, unicorn_exception_handler
from apps.core.error.validation_error import http422_error_handler, request_validation_exception_handler
from apps.core.events import create_start_app_handler, create_stop_app_handler
from apps.core.middle import init_middlewares
from apps.router import router as api_router
from apps.config.settings import (
    API_PREFIX,
    VERSION,
    PROJECT_NAME,
    DEBUG,
)


def create_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)

    # 添加事件
    application.add_event_handler("startup", create_start_app_handler(application))
    application.add_event_handler("shutdown", create_stop_app_handler(application))

    # 添加错误处理
    application.add_exception_handler(HTTPException, http_error_handler)
    application.add_exception_handler(RequestValidationError, http422_error_handler)
    application.add_exception_handler(RequestValidationError, request_validation_exception_handler)
    application.add_exception_handler(UnicornException, unicorn_exception_handler)

    # 添加中间件
    init_middlewares(application)

    # 添加路由
    application.include_router(api_router, prefix=API_PREFIX)
    return application
