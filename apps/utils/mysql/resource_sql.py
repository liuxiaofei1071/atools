# -*- coding: utf-8 -*- 
# @Time : 2020/10/16 17:40 
# @Author : Cadman
# @Email : liuxiaofeikeke@163.com
# @File : resource_sql.py

# 资源模型
from apps.core.db import db


def check_a_file(name):
    """校验去重"""
    sql = "SELECT COUNT(*) AS number FROM cc_resource WHERE `filename`=%s"
    result = db.get_one(sql, name)
    count = result.get("number")
    return True if count == 0 else False


def create_file(*args):
    """创建一个文件  resource_id, file_name, size, file_suffix, filename_full_path"""
    sql = """INSERT INTO cc_resource
                (`id`,`filename`,`size`,`suffix`,`path`,`create_by`,`create_time`,`update_by`,`update_time`)
            VALUES (%s,%s,%s,%s,%s,'admin',now(),'admin',now())"""
    return db.insert(sql, *args)
