# -*- coding: utf-8 -*- 
# @Time : 2020/10/12 14:03 
# @Author : Cassie Daddy  
# @Email : liuxiaofeikeke@163.com
# @File : mf_user.py

# 用户模型
from apps.core.db import db


# [用户账号密码管理组]

# 添加一组账号密码
def insert_sec_code(*args):
    sql = f"insert into sec_code(`id`,`user_id`,`cn_name`,`username`,`password`,`salt`,`create_time`,`remark`) \
          values('{args[0]}','{args[1]}','{args[2]}','{args[3]}',aes_encrypt('{args[4]}','{args[5]}'),'{args[5]}',now(),'{args[6]}')"
    return db.insert(sql)
#查询用户管理的所有账号密码

def get_user_code_list(id):
    sql = f"SELECT id, username,AES_DECRYPT(password,salt) as passwd,cn_name,remark FROM sec_code WHERE user_id='{id}'"
    return db.select(sql)

# 查询具体用户
def get_user_name(id):
    if id:
        sql = "select login_name from user_info where id={}".format(id)
        result = db.get_one(sql)
        return result
    else:
        return {}
