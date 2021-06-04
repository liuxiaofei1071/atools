# _*_coding: utf-8_*_
# @Time: 2020/11/22 16:17
# @Author: Cadman
# @Email: liuxiaofeikeke@163.com
# @File: hardware_service.py

from apps.utils.used.tools import Tools
from apps.utils.mysql import hardware_sql
from apps.core.base_response import UnicornException
from apps.core.error.code_total import ErrorCode, ErrorINFO


async def create(hardware_model):
    cn_name = hardware_model.cn_name
    en_name = hardware_model.en_name
    remark = hardware_model.remark
    parent_id = hardware_model.parent_id

    id = Tools.uid()
    ancestors = hardware_sql.get_ancestors_record(parent_id)
    if ancestors:
        ancestors += f",{parent_id}"
        level = len(ancestors.split(",")) - 1
        if hardware_sql.check_diff_record(cn_name, en_name, parent_id):
            hardware_sql.create_hardware_record(id, parent_id, ancestors, level, cn_name, en_name, remark)
        else:
            code = ErrorCode.select_already_exists
            raise UnicornException(code, ErrorINFO[code])
    else:
        code = ErrorCode.request_params_error
        raise UnicornException(code, ErrorINFO[code])


async def get_first_kind_list():
    """获取硬件库第一大类的所有信息"""
    result = hardware_sql.get_all_level_record(level=1)
    return result if result else []


async def get_kind_list():
    origin_list = hardware_sql.get_all_kind_record()
    print(origin_list,22)
    def get_tree(top_id):
        data = []
        for item in origin_list:
            if item['parent_id'] == top_id:
                next_pid = item['id']
                changed = {
                    "value": item["id"],
                    "label": item["cn_name"]
                }
                if next_pid in [i["parent_id"] for i in origin_list]:
                    changed['children'] = get_tree(next_pid)
                    data.append(changed)
                else:
                    get_tree(next_pid)
                    data.append(changed)
        return data

    result = get_tree("0")
    return result if result else []


async def get_second_kind_list(subkind):
    """获取硬件库所有第一大类的子类信息"""
    if subkind == "all":
        result = hardware_sql.get_all_level_record(2)
    else:
        result = hardware_sql.get_sub_kind_record(subkind, 2)
    return result if result else []
