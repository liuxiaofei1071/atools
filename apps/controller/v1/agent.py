# _*_ coding:utf-8 _*_
# @Time:2020/12/17 10:40
# @Author:Cadman
# @File agent.py

from typing import Optional
from fastapi import Query

from apps.core.base_response import success
from apps.service import agent_service
from apps.core.error.code_total import ErrorCode,ErrorINFO
from apps.core.base_response import fail
from apps.validator.model import ScriptItem


async def get_script_list():
    data = await agent_service.script_all()
    return success(data=data)

async def get_script_code(_id: Optional[str] = Query(None, min_length=3, max_length=50)):
    result = await agent_service.script_code(_id)
    return success(data=result)

async def create_script(py_model:ScriptItem):
    data = await agent_service.create(py_model)
    return success(data=data)

async def update_script():
    pass