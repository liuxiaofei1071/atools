# _*_ coding:utf-8 _*_
# @Time:2020/11/11 15:38
# @Author:Cadman
# @File events.py

from typing import Callable
from fastapi import FastAPI,Request


def create_start_app_handler(app: FastAPI) -> Callable:
    async def start_app() -> None:
        # 补充APP启动时需要的动作，例如：链接数据库
        pass
        return

    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:
    async def stop_app() -> None:
        # 补充APP关闭时需要的动作：例如关闭数据库
        pass

    return stop_app
