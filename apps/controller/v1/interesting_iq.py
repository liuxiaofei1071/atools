# _*_coding: utf-8_*_
# @Time: 2020/12/13 16:40
# @Author: Cadman
# @Email: liuxiaofeikeke@163.com
# @File: interesting_iq.py

from typing import Optional
from fastapi import Query

from apps.validator.model import IQValidateItem
from apps.service import validate_service
from apps.core.error.code_total import ErrorCode,ErrorINFO
from apps.core.base_response import success,fail

async def get_validate_list():
    data = await validate_service.get_all()
    return success(data=data)

async def create_validate(validate_model:IQValidateItem):
    await validate_service.create(validate_model)
    return success()

async def get_validate(
        _id: Optional[str] = Query(None, min_length=3, max_length=50)

):
    result = await validate_service.get_one(_id)
    if result is None:
        code = ErrorCode.select_resource_null
        return fail(code, msg=ErrorINFO[code])
    else:
        return success(data=result)

async def del_validate():
    pass

async def update_validate():
    pass