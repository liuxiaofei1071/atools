# _*_ coding:utf-8 _*_
# @Time:2020/12/17 10:47
# @Author:Cadman
# @File agent_service.py

import os

from apps.core.db_future import db
from apps.core.base_response import UnicornException
from apps.core.error.code_total import ErrorINFO,ErrorCode
from apps.utils.mysql.common_sql import CommonSQL,CommonFunc
from apps.utils.used.tools import Tools

async def read_list():
    script_list = db.fetch_all(CommonSQL.AGENT_SCRIPT_LIST)
    if script_list:
        for item in script_list:
            item['is_target_bind'] = "是" if item['is_target_bind'] else "否"
            item['is_alert_bind'] = "是" if item['is_alert_bind'] else "否"
            item['status'] = "有效" if item['status'] else "无效"
            cdt = item["create_time"]
            udt = item["update_time"]
            c_timer = f"{cdt.year}-{cdt.month}-{cdt.day} {cdt.hour}:{cdt.minute}:{cdt.second}"
            u_timer = f"{udt.year}-{udt.month}-{udt.day} {udt.hour}:{udt.minute}:{udt.second}"
            item['create_time'] = c_timer
            item['update_time'] = u_timer
    return script_list

async def script_detail(id):
    path = db.fetch_one(CommonSQL.AGENT_SCRIPT_CODE,id).get("path")
    if path and os.path.exists(path):
        if  path.endswith('.py'):
            with open(path,'r',encoding='utf-8') as f:
                content = f.read()

            return {"py_code":content}

        code = ErrorCode.py_resources_error
        raise UnicornException(code,ErrorINFO[code])
    else:
        code = ErrorCode.no_resources
        raise UnicornException(code,ErrorINFO[code])

async def create(py_model):
    _name = py_model.name
    _version = py_model.py_version
    _remark = py_model.remark
    _resource_id = py_model.resource_id
    _user = py_model.create_by

    id = Tools.uid
    status = CommonFunc.check_repeat(CommonSQL.AGENT_SCRIPT_CHECK,_name)
    if status:
        db.insert(CommonSQL.AGENT_SCRIPT_CREATE,id,_name,_version,_remark,_resource_id,_user)
    else:
        code = ErrorCode.select_already_exists
        raise UnicornException(code, ErrorINFO[code])

async def update(script_id,py_model):

    _name = py_model.name
    _version = py_model.py_version
    _remark = py_model.remark
    _status = py_model.status
    _user = py_model.create_by

    if db.update(CommonSQL.AGENT_SCRIPT_UPDATE, _name, _version, _status, _remark,_user,script_id):
        return ErrorCode.success
    code = ErrorCode.sql_execute_error
    raise UnicornException(code, ErrorINFO[code])




