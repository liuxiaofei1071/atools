# _*_ coding:utf-8 _*_
# @Time:2020/11/13 11:04
# @Author:Cadman
# @File host_server.py

from typing import Optional
from fastapi import Query

from apps.core.error.code_total import ErrorCode, ErrorINFO
from apps.core.base_response import fail
from apps.validator.model import HostServerItem, BindService
from apps.core.base_response import success
from apps.service import host_server_service


async def get_host_server_list():
    data = await host_server_service.get_all()
    return success(data=data)


async def create_host_server(
        host_server_model: HostServerItem
):
    await host_server_service.create_host_server(host_server_model)
    return success()


async def get_host_server(
        _id: Optional[str] = Query(None, min_length=3, max_length=50)

):
    result = await host_server_service.get_one(_id)
    if result is None:
        code = ErrorCode.select_resource_null
        return fail(code, msg=ErrorINFO[code])
    else:
        return success(data=result)


async def update_host_server(
        host_server_model: HostServerItem,
        _id: Optional[str] = Query(None, min_length=3, max_length=50)

):
    await host_server_service.update_one(host_server_model, _id)
    return success()
    pass


async def del_host_server(
        _id: Optional[str] = Query(None, min_length=3, max_length=50)
):
    await host_server_service.del_one(_id)
    return success()


async def bind_service(
        bind_service_model: BindService,
        _id: Optional[str] = Query(None, min_length=3, max_length=50)
):
    await host_server_service.bind(_id, bind_service_model)
    return success()
