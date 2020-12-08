# _*_coding: utf-8_*_
# @Time: 2020/11/22 15:26
# @Author: Cadman
# @Email: liuxiaofeikeke@163.com
# @File: hardware_kind.py

from typing import Optional
from fastapi import Query

from apps.validator.model import HardwareItem
from apps.service import hardware_service
from apps.core.base_response import success


async def hardware_create(
        hardware_model: HardwareItem
):
    data = await hardware_service.create(hardware_model)
    return success(data=data)


async def get_hardware_first_list():
    data = await hardware_service.get_first_kind_list()
    return success(data=data)


async def get_hardware_list():
    data = await hardware_service.get_kind_list()
    return success(data=data)


async def get_hardware_second_list(
        subkind: Optional[str] = Query(None, min_length=3, max_length=50)
):
    data = await hardware_service.get_second_kind_list(subkind)
    return success(data=data)
