# -*- coding: utf-8 -*-
# @Time : 2020/9/21 12:02
# @Author : Cassie Daddy
# @Email : liuxiaofeikeke@163.com
# @Site :
# @File : files_manager.py

from fastapi import APIRouter

router = APIRouter()

from apps.controller import files_manager
from apps.controller import driver_curd
