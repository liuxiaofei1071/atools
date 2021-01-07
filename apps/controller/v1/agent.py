# _*_ coding:utf-8 _*_
# @Time:2020/12/17 10:40
# @Author:Cadman
# @File agent.py

from typing import Optional
from fastapi import Query

from apps.core.base_response import success
from apps.service import agent_service
from apps.validator.model import ScriptModel, ScriptUpdateModel,AgentCode


async def get_script_list():
    data = await agent_service.read_list()
    return success(data=data)


async def create_script(py_model: ScriptModel):
    data = await agent_service.create(py_model)
    return success(data=data)


async def update_script(*, script_id: Optional[str] = Query(None, min_length=3, max_length=50),
                        py_model: ScriptUpdateModel):
    await agent_service.update(script_id, py_model)
    return success()


async def del_script(script_id: Optional[str] = Query(None, min_length=3, max_length=50)):
    await agent_service.delete(script_id)
    return success()


async def get_script(script_id: Optional[str] = Query(None, min_length=3, max_length=50)):
    data = await agent_service.read(script_id)
    return success(data=data)

# # code
async def get_script_code(_id: Optional[str] = Query(None, min_length=3, max_length=50)):
    result = await agent_service.code_detail(_id)
    return success(data=result)


async def update_script_code(*,code_id: Optional[str] = Query(None, min_length=3, max_length=50),code_model:AgentCode):
    await agent_service.update_code(code_id,code_model)
    return success()