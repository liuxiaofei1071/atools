# -*- coding: utf-8 -*- 
# @Time : 2020/10/12 13:33 
# @Author : Cadman
# @Email : liuxiaofeikeke@163.com
# @File : user_sql.py

from typing import Optional
from fastapi import Query

from apps.core.base_response import success
from apps.service import user_service
from apps.validator.model import SecCode, LoginItem


async def get_sec_code_list(
        _id: Optional[str] = Query(None, min_length=3, max_length=50)
):
    data = await user_service.sec_list(_id)
    return success(data=data)


async def create_sec_code(sec_model: SecCode):
    await user_service.create(sec_model)
    return success()


async def update_sec_code():
    pass


async def login(
        login_model: LoginItem
):
    await user_service.login_service(login_model)
    return success()


async def rsa():
    data = await user_service.generate_rsa()
    return success(data=data)
