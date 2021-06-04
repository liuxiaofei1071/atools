# _*_ coding:utf-8 _*_
# @Time:2021/2/23 15:32
# @Author:Cassie·Lau
# @File urls.py

"""App v2 Router"""

from fastapi import APIRouter

from apps.controller.v2 import (
    devops,

)
router = APIRouter()

#[Paas]
router.get(path="/directory",tags=["server dir"])(devops.is_dir)


