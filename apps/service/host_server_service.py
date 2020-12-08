# _*_ coding:utf-8 _*_
# @Time:2020/11/14 11:49
# @Author:Cadman
# @File host_server_service.py

from apps.core.error.code_total import ErrorINFO, ErrorCode
from apps.core.base_response import UnicornException
from apps.utils.mysql import host_server_sql
from apps.utils.used.tools import Tools


async def create_host_server(
        host_server_model
):
    server_name = host_server_model.name
    server_ip = host_server_model.ip
    version = host_server_model.version
    memory = host_server_model.memory
    cpu = host_server_model.cpu
    sys_status = host_server_model.status
    effect = host_server_model.effect
    sys_check = host_server_model.sys_check
    remarks = host_server_model.remarks

    id = Tools.uid()
    status = host_server_sql.check_host_server_record(server_name, server_ip)
    if status:
        host_server_sql.create_host_server_record(id, server_name, server_ip, version, memory, cpu, sys_status, effect,
                                                  sys_check, remarks)
    else:
        code = ErrorCode.select_already_exists
        raise UnicornException(code, ErrorINFO[code])
    return


async def get_all():
    result = host_server_sql.select_all_host_server_record()
    return result if result else []


async def get_one(id):
    result = host_server_sql.select_host_server_record_by_id(id)
    return result if result else None


async def del_one(id):
    host_server_sql.select_host_server_record_by_id(id)
    return


async def update_one(host_server_model, id):
    server_name = host_server_model.name
    server_ip = host_server_model.ip
    version = host_server_model.version
    memory = host_server_model.memory
    cpu = host_server_model.cpu
    sys_status = host_server_model.status
    effect = host_server_model.effect
    sys_check = host_server_model.sys_check
    remarks = host_server_model.remarks
    host_server_sql.update_host_server_record(server_name, server_ip, version, memory, cpu, sys_status,
                                              effect, sys_check, remarks, id)
    return


async def bind(id, bind_service_model):
    services = bind_service_model.services
    service_list = [] if None in services else services
    if service_list:
        s_tuple = [(id, service_id) for service_id in service_list]

        host_server_sql.create_server__service_record(s_tuple)
        return
    else:
        code = ErrorCode.server_not_bind_services
        raise UnicornException(code, ErrorINFO[code])
