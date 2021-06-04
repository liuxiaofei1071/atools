# _*_ coding:utf-8 _*_
# @Time:2020/11/2 12:57
# @Author:Cadman
# @File router.py

from fastapi import APIRouter

from apps.routers.v1 import urls as app_v1
from apps.routers.v2 import urls as app_v2
from apps.controller.v1 import websocket_server

router = APIRouter()
router.websocket(path="/ws/{user}",)(websocket_server.websocket_endpoint)

router.include_router(app_v1.router, prefix="/api/v1")
router.include_router(app_v2.router, prefix="/api/v2")




