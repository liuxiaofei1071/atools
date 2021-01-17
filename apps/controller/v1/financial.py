# _*_coding: utf-8_*_
# @Time: 2021/1/17 22:52
# @Author: Cadman
# @Email: liuxiaofeikeke@163.com
# @File: financial.py

from typing import Optional
from fastapi import Query

from apps.core.base_response import success
from apps.service import financial_service
from apps.validator.model import FamilyBillModel,FamilyBillUpdateModel

async def get_bill_list():
    data = await financial_service.read_bill_list()
    return success(data=data)


async def create_bill(bill_model: FamilyBillModel):
    data = await financial_service.create_bill(bill_model)
    return success(data=data)


async def update_bill(*, bill_id: Optional[str] = Query(None, min_length=3, max_length=50),
                        bill_model: FamilyBillUpdateModel):
    await financial_service.update(bill_id, bill_model)
    return success()


async def del_bill(bill_id: Optional[str] = Query(None, min_length=3, max_length=50)):
    await financial_service.delete(bill_id)
    return success()


async def get_bill(bill_id: Optional[str] = Query(None, min_length=3, max_length=50)):
    data = await financial_service.read(bill_id)
    return success(data=data)