# _*_ coding:utf-8 _*_
# @Time:2020/11/14 11:50
# @Author:Cadman
# @File host_server_sql.py
from apps.core.db_future import db


# def create_host_server_record(id, name, ip, version, memory, cpu, sys_status, effect, sys_check, remark):
def create_host_server_record(*args):
    """添加一种文件类型"""
    sql = """INSERT INTO sys_host_server(`id`,`server_name`,`server_ip`,`sys_version`,`memory`,`cpu`,
                        `status`,`effect`,`sys_check`,`remark`,`create_time`,`create_by`,`update_time`,`update_by`)
             VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,NOW(),'admin',NOW(),'admin')
          """
    # params_list = [id, name, ip, version, memory, cpu, sys_status, effect, sys_check, remark]
    return db.insert(sql, *args)


def check_host_server_record(name, ip):
    """文件类型校验去重"""
    sql = "SELECT COUNT(*) as number  FROM sys_host_server WHERE `server_name`=%s AND `server_ip`=%s"
    result = db.get_one(sql, name,ip)
    count = result.get("number")
    return True if count == 0 else False


def select_all_host_server_record():
    sql = """SELECT 
                `id`,`server_ip`,`server_name`,
                CASE WHEN `status`='0' THEN "有效" ELSE "无效" END as sys_status,
                CASE WHEN `effect`='0' THEN "开发" 
                     WHEN `effect`='1' THEN "测试" 
                     WHEN  `effect`='2' THEN "预生产"
                     ELSE "生产"
                END as sys_effect,
                CASE WHEN `sys_check`='0' THEN "逻辑服务器" ELSE "网关服务器" END as checks,
                `memory`,
                `cpu`,
                `remark`,
                `create_time`,
                `update_time`
            FROM sys_host_server
        """
    return db.select(sql)


def select_host_server_record_by_id(id):
    sql = """SELECT `id`,`server_ip`,`server_name`,`memory`,
                    `cpu`,`remark`,`create_time`,update_time,
                    CASE WHEN `status`='0' THEN "有效" ELSE "无效" END as sys_status,
                    CASE WHEN `effect`='0' THEN "开发" 
                         WHEN `effect`='1' THEN "测试" 
                         WHEN  `effect`='2' THEN "预生产"
                         ELSE "生产"
                         END as sys_effect,
                    CASE WHEN `sys_check`='0' THEN "逻辑服务器" ELSE "网关服务器" END as checks
            FROM sys_host_server WHERE `id`=%s
         """
    result = db.get_one(sql, id)
    return result


def del_one_record(id):
    sql = "DELETE FROM sys_host_server WHERE id=%s"
    return db.delete(sql, id)


def update_host_server_record(*args):
    sql = """UPDATE 
                sys_host_server 
            SET `server_name`=%s,
                `server_ip`=%s,
                `sys_version`=%s,
                `memory`=%s,
                `cpu`=%s,
                `status`=%s,
                `effect`=%s,
                `sys_check`=%s,
                `remark`=%s,
                `update_time`=Now() 
            WHERE `id`=%s"""
    return db.update(sql, *args)

def create_server__service_record(ss_tuple):
    sql = """INSERT INTO server__service(`server_id`,`service_id`)VALUES(%s,%s) """
    return db.insert_more(sql,ss_tuple)