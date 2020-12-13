# _*_coding: utf-8_*_
# @Time: 2020/12/13 20:59
# @Author: Cadman
# @Email: liuxiaofeikeke@163.com
# @File: validate_service.py

from apps.core.base_response import UnicornException
from apps.core.error.code_total import ErrorCode,ErrorINFO
from apps.utils.used.tools import Tools
from apps.utils.mysql.common_sql import CommonSQL,CommonFunc
from apps.core.db_future import db

async def create(validate_model):
    question = validate_model.question
    answer = validate_model.answer
    remark = validate_model.remark

    id = Tools.uid()
    status = CommonFunc.kill_repeat(CommonSQL.IQ_VALIDATE_DIFF_BY_QUESTION,question)
    if status:
        db.insert(CommonSQL.IQ_VALIDATE_CREATE,id, question, answer, remark)
    else:
        code = ErrorCode.select_already_exists
        raise UnicornException(code, ErrorINFO[code])


async def get_all():
    result = db.fetch_all(CommonSQL.IQ_VALIDATE_LIST)
    return result if result else []

async def get_one(id):
    result = db.fetch_one(CommonSQL.IQ_VALIDATE_BY_ID,id)
    return result if result else None

