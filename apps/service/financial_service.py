# _*_coding: utf-8_*_
# @Time: 2021/1/17 23:06
# @Author: Cadman
# @Email: liuxiaofeikeke@163.com
# @File: financial_service.py

from apps.core.db.database import db
from apps.utils.mysql.common_sql import CommonSQL
from apps.utils.used.tools import Tools
from apps.core.error.code_total import StatusCode
from apps.core.base_response import UnicornException

async def read_bill_list():

    bill_list = db.fetch_all(CommonSQL.BILL_LIST)

    if bill_list:
        for item in bill_list:
            item['create_time'] = Tools.date_format(item['create_time'])
            item['update_time'] = Tools.date_format(item['update_time']) if item['update_time'] else "暂无"
    return bill_list

async def create_bill(bill_model):
    _title = bill_model.title
    _money = bill_model.money
    _remark = bill_model.remark
    _payway = bill_model.payway
    _expenses_kind_id = bill_model.expenses_kind_id
    _user = bill_model.create_by

    id = Tools.uid()
    status = db.fetch_one(CommonSQL.BILL_CHECK, _title).get("number")
    if status == 0:
        _user_id = db.fetch_one(CommonSQL.GET_USER_ID, _user)
        if _user_id:
            user_id = _user_id.get("id")
            db.insert(CommonSQL.BILL_CREATE, id, _title, _expenses_kind_id, _payway, _money,_remark, user_id)
        else:
            raise UnicornException(StatusCode.P40001["code"], StatusCode.P40001["msg"])
    else:
        raise UnicornException(StatusCode.R20001["code"], StatusCode.R20001["msg"])