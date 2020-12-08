# _*_ coding:utf-8 _*_
# @Time:2020/11/11 16:14
# @Author:Cadman
# @File content_type_service.py

from apps.core.base_response import UnicornException
from apps.core.error.code_total import ErrorCode, ErrorINFO
from apps.utils.used.tools import Tools
from apps.utils.mysql import content_type_sql


async def create(
        content_type_model
):
    name = content_type_model.name
    file_type = content_type_model.file_type
    suffix = content_type_model.suffix

    id = Tools.uid()
    status = content_type_sql.check_record(file_type, suffix)
    if status:
        content_type_sql.create_record(id, file_type, name, suffix)
    else:
        code = ErrorCode.select_already_exists
        raise UnicornException(code, ErrorINFO[code])


async def get_one(id):
    result = content_type_sql.select_record_by_id(id)
    return result if result else None


async def get_all():
    result = content_type_sql.select_all_record()
    return result if result else []


async def del_one(id):
    content_type_sql.del_one_record(id)
    return
