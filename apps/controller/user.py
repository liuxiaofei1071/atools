# -*- coding: utf-8 -*- 
# @Time : 2020/10/12 13:33 
# @Author : Cassie Daddy  
# @Email : liuxiaofeikeke@163.com
# @File : mf_user.py

from apps.controller import router
from apps.model.m_user import SecCode
from apps.utils.used.tools import Tools
from apps.core.r_code import RESPONSE,RESPONSE_LIST
from apps.utils.mysql import mf_user

@router.get("/code/list/{user_id}",tags=["user"])
async def get_sec_code_list(user_id:str):
    if user_id:
        result = mf_user.get_user_code_list(user_id)
        if not result :
            RESPONSE_LIST["error"] = "当前用户查询失败"
        for item in result:
            item["passwd"] = Tools.base64_decode(item["passwd"])
        RESPONSE_LIST["data"] = result
    else:
        RESPONSE_LIST["error"] = "用户参数不存在"
    return RESPONSE_LIST


@router.post("/code/{user_id}",status_code=200,tags=["user"])
async def create_sec_code(user_id:str,item:SecCode):
    cn_name = item.cn_name
    username = item.username
    password = Tools.base64_encode(item.password)
    remark = item.remark
    id = Tools.uid()
    login_name_dict = mf_user.get_user_name(user_id)
    if login_name_dict:
        login_name = login_name_dict.get("login_name")
        salt = Tools.sha1_salt(login_name)
        result = mf_user.insert_sec_code(id, user_id, cn_name, username, password, salt, remark)
        if result != 0:
            RESPONSE["data"]["success"] = "false"
            RESPONSE["error"] = "插入数据库失败"
    else:
        RESPONSE["data"]["success"] = "false"
        RESPONSE["error"] = "当前用户不存在"

    return RESPONSE