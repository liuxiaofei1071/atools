# _*_ coding:utf-8 _*_
# @Time:2020/11/2 17:08
# @Author:Cadman
# @File http_error.py

from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse

from apps.core.base_response import UnicornException


async def http_error_handler(_: Request, exc: HTTPException):
    return JSONResponse(
        {
            "code": exc.status_code,
            "message": exc.detail,
            "data": exc.detail
        }, status_code=exc.status_code
    )


async def unicorn_exception_handler(_: Request, exc: UnicornException):
    return JSONResponse({
        "code": exc.code,
        "message": exc.errmsg,
        "data": exc.data,
    })
