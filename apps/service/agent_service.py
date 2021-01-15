# _*_ coding:utf-8 _*_
# @Time:2020/12/17 10:47
# @Author:Cadman
# @File agent_service.py

import os

from apps.core.db.database import db
from apps.core.base_response import UnicornException
from apps.core.error.code_total import StatusCode
from apps.utils.mysql.common_sql import CommonSQL
from apps.utils.used.tools import Tools

async def read_list():
    script_list = db.fetch_all(CommonSQL.AGENT_SCRIPT_LIST)

    if script_list:
        for item in script_list:
            item['is_target_bind'] = "是" if item['is_target_bind'] else "否"
            item['is_alert_bind'] = "是" if item['is_alert_bind'] else "否"
            item['status'] = "有效" if item['status'] else "无效"
            item['create_time'] = Tools.date_format(item['create_time'])
            item['update_time'] = Tools.date_format(item['update_time']) if item['update_time'] else "暂无"
    return script_list


async def create(py_model):
    _name = py_model.name
    _version = py_model.py_version
    _remark = py_model.remark
    _resource_id = py_model.resource_id
    _user = py_model.create_by

    id = Tools.uid()
    status = db.fetch_one(CommonSQL.AGENT_SCRIPT_CHECK,_name).get("number")
    if status == 0:
        _user_id = db.fetch_one(CommonSQL.GET_USER_ID,_user)
        if _user_id:
            user_id = _user_id.get("id")
            db.insert(CommonSQL.AGENT_SCRIPT_CREATE,id,_name,_version,_remark,_resource_id,user_id)
        else:
            raise UnicornException(StatusCode.P40001["code"],StatusCode.P40001["msg"])
    else:
        raise UnicornException(StatusCode.R20001["code"],StatusCode.R20001["msg"])

async def update(script_id,py_model):

    _name = py_model.name
    _version = py_model.py_version
    _remark = py_model.remark
    _status = py_model.status
    _user = py_model.update_by
    if db.fetch_one(CommonSQL.AGENT_SCRIPT_ONE,script_id):
        db.update(CommonSQL.AGENT_SCRIPT_UPDATE, _name, _version, _status, _remark,_user,script_id)
    else:
        raise UnicornException(StatusCode.R20006["code"],StatusCode.R20006["msg"])


async def delete(script_id):
    script_info =  db.fetch_one(CommonSQL.AGENT_SCRIPT_ONE, script_id)
    if script_info:
        db.delete(CommonSQL.AGENT_SCRIPT_DEL,script_id)
    else:
        raise UnicornException(StatusCode.R20006["code"], StatusCode.R20006["msg"])

async def read(script_id):

    result = db.fetch_one(CommonSQL.AGENT_SCRIPT_ONE,script_id,0)
    if result:
        return result
    else:
        raise UnicornException(StatusCode.R20002["code"], StatusCode.R20002["msg"])

# ---------------------------------------------------------------------------------------
# code
async def code_detail(id):
    _path = db.fetch_one(CommonSQL.AGENT_SCRIPT_CODE,id)
    if _path:
        path = _path.get("path")
        print(path,111)
        if os.path.exists(path):
            with open(path,'r',encoding='utf-8') as f:
                content = f.read()
            return {"py_code":content}
        raise UnicornException(StatusCode.R20005["code"], StatusCode.R20005["msg"])
    else:
        raise UnicornException(StatusCode.R20002["code"],StatusCode.R20002["msg"])

async def update_code(id,code_model):
    code = code_model.code
    _path = db.fetch_one(CommonSQL.AGENT_SCRIPT_CODE, id)
    if _path:
        path = _path.get("path")
        if os.path.exists(path):
            with open(path, 'w', encoding='utf-8') as f:
                f.write(code)
        else:
            raise UnicornException(StatusCode.R20005["code"], StatusCode.R20005["msg"])
    else:
        raise UnicornException(StatusCode.R20002["code"], StatusCode.R20002["msg"])