# -*- coding: utf-8 -*- 
# @Time : 2020/10/12 14:03 
# @Author : Cadman
# @Email : liuxiaofeikeke@163.com
# @File : user_sql.py

# 用户模型
from apps.core.db_future import db


# [用户账号密码管理组]


def create_sec_code(*args):
    """
    添加一组账号密码
    """
    sql = """INSERT INTO 
                sec_code(`id`,`user_id`,`cn_name`,`username`,`password`,`salt`,`create_time`,`remark`) 
             VALUES (%s,%s,%s,%s,aes_encrypt(%s,%s),%s,NOW(),%s)"""
    return db.insert(sql, *args)



def get_user_code_list(id):
    """
    查询用户管理的所有账号密码
    """
    sql = """SELECT 
                `id`, `username`,AES_DECRYPT(`password`,`salt`) AS `passwd`,`cn_name`,`remark` 
            FROM sec_code WHERE `user_id`= %s"""
    return db.fetch_all(sql, id)



def get_user_name(id):
    """
    查询具体用户
    """
    sql = "SELECT `nick_name` FROM todo_user WHERE `id`= %s"
    record = db.fetch_one(sql, id)
    result = record.get("login_name", "")
    return result

def check_sec_record(cn_name):
    """
    校验去重秘钥类型
    """
    sql = "SELECT COUNT(*) AS number FROM  sec_code WHERE `cn_name`= %s"
    result = db.fetch_one(sql,cn_name)
    count = result.get("number")
    return True if count == 0 else False


def create_rsa_record(*args):
    """
    创建一条rsa记录
    """
    sql = "INSERT INTO todo_rsa(ID, `PRIVATE_KEY`, `CREATE_TIME`) VALUES (%s,%s,NOW())"
    return db.insert(sql,*args)

def get_rsa_record(access_id):
    """
    获取rsa
    """
    sql = "SELECT `private_key` FROM todo_rsa WHERE `id`=%s"
    result =  db.fetch_one(sql, access_id)
    private_key = result.get("private_key","")
    return private_key if private_key else False

def check_auth_record(username):
    sql = """
            SELECT `identifier`,`password` FROM todo_user_auth WHERE `identifier`=%s
    """
    return db.fetch_one(sql,username)

def check_user_status_record(username):
    sql = """
        SELECT status FROM todo_user  WHERE `ID`=(SELECT `user_id` FROM todo_user_auth WHERE `identifier`=%s) AND is_del=%s
    """
    result = db.fetch_one(sql,(username,0))
    status = result.get("status") if result else False
    return True if status!=False else status

def del_rsa_record(_id):
    sql = "DELETE FROM todo_rsa WHERE id=%s"
    return db.delete(sql,_id)