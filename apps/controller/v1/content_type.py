# _*_ coding:utf-8 _*_
# @Time:2020/10/27 15:36
# @Author:Cadman
# @File content_type.py

from typing import Optional
from fastapi import Query

from apps.core.base_response import success, fail
from apps.validator.model import ContentTypeItem
from apps.core.error.code_total import ErrorCode, ErrorINFO
from apps.service import content_type_service


async def create_content_type(
        content_type_model: ContentTypeItem
):
    await content_type_service.create(content_type_model)
    return success()


async def get_content_type(
        _id: Optional[str] = Query(None, min_length=3, max_length=50)
):
    result = await content_type_service.get_one(_id)
    if result is None:
        code = ErrorCode.select_resource_null
        return fail(code, msg=ErrorINFO[code])
    else:
        return success(data=result)


async def get_content_type_list():
    data = await content_type_service.get_all()
    return success(data=data)


async def del_content_type(
        _id: Optional[str] = Query(None, min_length=3, max_length=50)
):
    await content_type_service.del_one(_id)
    return success()
