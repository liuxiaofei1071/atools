# -*- coding: utf-8 -*- 
# @Time : 2020/10/16 17:40 
# @Author : Cassie Daddy  
# @Email : liuxiaofeikeke@163.com
# @File : mf_resource.py

# 资源模型
from apps.core.db import db


def check_a_file(name):
    """校验去重"""
    sql = f"select count(*) as number from cc_resource where filename='{name}'"
    result = db.get_one(sql)
    count = result.get("number")
    return True if count == 0 else False


def create_file(*args):
    """添加歌曲"""
    sql = f"INSERT INTO cc_resource(`id`,`filename`,`size`,`suffix`,`path`,`create_by`,`create_time`,`update_by`,`update_time`) \
          VALUES ('{args[0]}','{args[1]}','{args[2]}','{args[3]}','{args[4]}','admin',now(),'admin',now())"
    return db.insert(sql)
