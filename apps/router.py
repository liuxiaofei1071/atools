# _*_ coding:utf-8 _*_
# @Time:2020/11/2 12:57
# @Author:Cadman
# @File router.py

from fastapi import APIRouter

from apps.routers.v1 import urls as app_v1

router = APIRouter()
router.include_router(app_v1.router, prefix="/v1")
