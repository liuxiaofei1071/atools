# _*_coding: utf-8_*_
# @Time: 2020/12/13 23:24
# @Author: Cadman
# @Email: liuxiaofeikeke@163.com
# @File: common_sql.py
from apps.core.db_future import db


class CommonSQL:
    """
    sql语句集散中心
    """

    #用户
    GET_USER_ID = "SELECT `id` FROM todo_user WHERE `id`=%s"


    # IQ_validate
    IQ_VALIDATE_GET_LIST = """SELECT `id`,`question`,`answer`,`remark`,`kind`,`create_time` FROM coco_home.todo_interesting_poetry"""
    IQ_VALIDATE_GET_ONE = """SELECT `id`,`question`,`kind` FROM coco_home.todo_interesting_poetry WHERE `id`=%s AND `status`=1 AND `is_used`=0"""
    IQ_VALIDATE_CREATE = """INSERT INTO coco_home.todo_interesting_poetry
                                (`id`,`question`,`answer`,`remark`,`kind`,`create_by`,`create_time`)
                            VALUES (%s,%s,%s,%s,%s,%s,NOW())"""
    IQ_VALIDATE_CHECK = """SELECT COUNT(*) as number  FROM coco_home.todo_interesting_poetry
                                      WHERE `question`=%s"""
    IQ_VALIDATE_DEL_ONE = "DELETE FROM coco_home.todo_interesting_poetry WHERE id=%s"
    IQ_VALIDATE_UPDATE_ONE = """UPDATE coco_home.todo_interesting_poetry 
                                SET `question`=%s,`answer`=%s,`remark`=%s,`update_time`=Now() 
                                WHERE `id`=%s"""
    IQ_VALIDATE_ALL_ID = """SELECT `id` FROM coco_home.todo_interesting_poetry"""
    IQ_VALIDATE_ANSWER = """SELECT `answer` FROM coco_home.todo_interesting_poetry WHERE id=%s AND answer=%s"""

    # py相关
    AGENT_SCRIPT_LIST = "SELECT * FROM cocoa.drive_py_script WHERE `is_del`=0"
    AGENT_SCRIPT_CODE = """SELECT path FROM cocoa.cc_resource 
                            WHERE `id` =(SELECT resource_id FROM cocoa.drive_py_script WHERE id=%s AND `status`=1)"""
    AGENT_SCRIPT_CREATE = """INSERT INTO drive_py_script(`id`,`name`,`py_version`,`remark`,`resource_id`,
                                `create_time`,`create_by`)VALUES (%s,%s,%s,%s,%s,NOW(),%s)"""
    AGENT_SCRIPT_CHECK = "SELECT COUNT(*) as number  FROM cocoa.drive_py_script WHERE `name`=%s"

    AGENT_SCRIPT_UPDATE = """UPDATE cocoa.drive_py_script 
                                SET  `name`=%s,`py_version`=%s,`status`=%s,`remark`=%s,`update_by`=%s,`update_time`=Now() 
                                WHERE `id`=%s"""

    AGENT_SCRIPT_ONE = "SELECT * FROM drive_py_script WHERE `id`=%s AND is_del=0"
    AGENT_SCRIPT_DEL = "DELETE FROM cocoa.drive_py_script WHERE id=%s"

class CommonFunc:
    @staticmethod
    def check_repeat(sql, *args):
        """文件类型校验去重"""
        result = db.fetch_one(sql, args)
        count = result.get("number")
        return True if count == 0 else False
