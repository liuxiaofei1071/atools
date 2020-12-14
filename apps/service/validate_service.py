# _*_coding: utf-8_*_
# @Time: 2020/12/13 20:59
# @Author: Cadman
# @Email: liuxiaofeikeke@163.com
# @File: validate_service.py
import random

from apps.core.db_future import db
from apps.core.base_response import UnicornException
from apps.core.error.code_total import ErrorCode, ErrorINFO
from apps.utils.used.tools import Tools
from apps.utils.mysql.common_sql import CommonSQL, CommonFunc


async def create(validate_model):
    question = validate_model.question
    answer = validate_model.answer
    remark = validate_model.remark

    id = Tools.uid()
    status = CommonFunc.kill_repeat(CommonSQL.IQ_VALIDATE_DIFF_BY_QUESTION, question)
    if status:
        db.insert(CommonSQL.IQ_VALIDATE_CREATE, id, question, answer, remark)
    else:
        code = ErrorCode.select_already_exists
        raise UnicornException(code, ErrorINFO[code])


async def get_all():
    result = db.fetch_all(CommonSQL.IQ_VALIDATE_GET_LIST)
    return result if result else []


async def get_one(id):
    result = db.fetch_one(CommonSQL.IQ_VALIDATE_GET_ONE, id)
    return result if result else None


async def del_one(id):
    if db.delete(CommonSQL.IQ_VALIDATE_DEL_ONE, id):
        return ErrorCode.success
    code = ErrorCode.sql_execute_error
    raise UnicornException(code, ErrorINFO[code])


async def update_one(validate_model, _id):
    question = validate_model.question
    answer = validate_model.answer
    remark = validate_model.remark
    if db.update(CommonSQL.IQ_VALIDATE_UPDATE_ONE, question, answer, remark, _id):
        return ErrorCode.success
    code = ErrorCode.sql_execute_error
    raise UnicornException(code, ErrorINFO[code])

async def random_question():

    question_list = db.fetch_all(CommonSQL.IQ_VALIDATE_ALL_ID)
    if question_list:
        random_id = random.choice(question_list).get('id')
        return db.fetch_one(CommonSQL.IQ_VALIDATE_GET_ONE,random_id)
    code = ErrorCode.no_resources
    raise UnicornException(code,ErrorINFO[code])

async def answer(answer_model):
    id = answer_model.id
    answer = answer_model.answer
    result = db.fetch_one(CommonSQL.IQ_VALIDATE_ANSWER,id,answer)
    if result:
        return ErrorCode.success
    code = ErrorCode.IQ_verification_failed
    raise UnicornException(code,ErrorINFO[code])

