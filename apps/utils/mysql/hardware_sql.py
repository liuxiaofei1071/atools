# _*_coding: utf-8_*_
# @Time: 2020/11/22 20:54
# @Author: Cadman
# @Email: liuxiaofeikeke@163.com
# @File: hardware_sql.py

from apps.core.db.database import db


def create_hardware_record(*args):
    """添加一条硬件库类型记录"""
    sql = """INSERT INTO sys_kinds (`id`,`parent_id`,`ancestors`,`level`,`cn_name`,
                        `en_name`,`remark`,`create_time`,`create_by`)
             VALUES (%s,%s,%s,%s,%s,%s,%s,NOW(),'admin')
          """

    return db.insert(sql, *args)


def get_ancestors_record(parent_id):
    sql = "SELECT `ancestors` FROM sys_kinds WHERE `id`=%s"
    _ancestors_dict = db.fetch_one(sql, parent_id)
    result = _ancestors_dict.get("ancestors", "")
    return result if result else False


def check_diff_record(cn_name, en_name,parent_id):
    """硬件库类型校验去重"""
    sql = "SELECT COUNT(*) as number  FROM sys_kinds WHERE `cn_name`=%s AND `en_name`= %s AND `parent_id`=%s"
    result = db.fetch_one(sql, cn_name, en_name,parent_id)
    count = result.get("number")
    return True if count == 0 else False

def get_all_level_record(level):
    sql = """SELECT 
                `id`,`cn_name`,`parent_id`,`en_name`,`remark`,`status`,`create_by` 
             FROM sys_kinds WHERE  `is_del`=0  AND `level`=%s"""
    return db.fetch_all(sql,level)

def get_all_kind_record():
    sql = """SELECT id,parent_id,ancestors,cn_name FROM sys_kinds WHERE  `is_del`=0"""
    return db.fetch_all(sql)

def get_sub_kind_record(subkind,level):
    sql = """
    SELECT `id`,`en_name`,`cn_name`,`remark`,`status`,`create_by` FROM sys_kinds 
        WHERE parent_id in (SELECT id FROM sys_kinds WHERE `is_del`=0 AND en_name=%s) 
        AND level=%s 
    """
    params_t = (subkind,level)
    return db.fetch_all(sql,params_t)
