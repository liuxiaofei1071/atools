# _*_ coding:utf-8 _*_
# @Time:2020/11/2 12:35
# @Author:Cadman
# @File validation_error.py

from typing import Union
from pydantic import ValidationError
from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from apps.config.settings import logger


async def http422_error_handler(_: Request, exc: Union[RequestValidationError, ValidationError], ) -> JSONResponse:
    return JSONResponse(
        {
            "code": status.HTTP_422_UNPROCESSABLE_ENTITY,
            "message": "参数校验错误",
            "data": exc.errors(),
        },
        status_code=422,
    )


async def request_validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.error(f"参数错误{request.method} {request.url}")
    return JSONResponse(
        {
            "code": status.HTTP_400_BAD_REQUEST,
            "message": "请求参数校验异常",
            "data": exc.errors()
        }
    )
