# _*_ coding:utf-8 _*_
# @Time:2020/10/27 15:47
# @Author:Cadman
# @File content_type_sql.py

# 文件类型模型
from apps.core.db import db


# [类型管理组]

def create_record(*args):
    """添加一种文件类型"""
    sql = """INSERT INTO cc_content_type(`id`,`filetype`,`name`,`suffix`,`create_time`,`create_by`,`update_time`,`update_by`)
          VALUES (%s,%s,%s,%s,NOW(),'admin',NOW(),'admin')"""
    return db.insert(sql, *args)


def select_record_by_id(cid):
    """查询具体文件类型"""
    sql = "SELECT `id`,`filetype`,`name`,`suffix` FROM cc_content_type WHERE `id`=%s"
    result = db.get_one(sql, cid)
    return result


def select_all_record():
    """查询所有文件类型"""
    sql = "SELECT `id`,`filetype`,`name`,`suffix` FROM cc_content_type"
    return db.select(sql)
    # return result if result else []


def check_record(*args):
    """文件类型校验去重"""
    sql = "SELECT COUNT(*) as number  FROM cc_content_type WHERE `filetype`=%s AND `suffix`=%s"
    result = db.get_one(sql, *args)
    count = result.get("number")
    return True if count == 0 else False


def select_content_dir_record(*args):
    """获取目录名称"""
    sql = "SELECT `name` FROM cc_content_type WHERE `filetype`=%s AND `suffix`=%s"
    result = db.get_one(sql, *args)
    return result


def del_one_record(_id):
    sql = "DELETE FROM cc_content_type WHERE id=%s"
    return db.delete(sql, _id)
