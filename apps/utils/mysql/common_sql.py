# _*_coding: utf-8_*_
# @Time: 2020/12/13 23:24
# @Author: Cadman
# @Email: liuxiaofeikeke@163.com
# @File: common_sql.py
from apps.core.db_future import db

class CommonSQL:
    """
    all sql语句集散中心
    """

    # IQ_validate
    IQ_VALIDATE_GET_LIST = """SELECT `id`,`question`,`answer`,`remark`,`create_time` FROM coco_home.todo_interesting_poetry"""
    IQ_VALIDATE_GET_ONE = """SELECT `id`,`question` FROM coco_home.todo_interesting_poetry WHERE `id`=%s AND `status`=0 AND `is_used`=0"""
    IQ_VALIDATE_CREATE = """INSERT INTO coco_home.todo_interesting_poetry
                                (`id`,`question`,`answer`,`remark`,`create_time`,`create_by`)
                            VALUES (%s,%s,%s,%s,NOW(),'admin')"""
    IQ_VALIDATE_DIFF_BY_QUESTION = """SELECT COUNT(*) as number  FROM coco_home.todo_interesting_poetry
                                      WHERE `question`=%s"""
    IQ_VALIDATE_DEL_ONE = "DELETE FROM coco_home.todo_interesting_poetry WHERE id=%s"
    IQ_VALIDATE_UPDATE_ONE = """UPDATE coco_home.todo_interesting_poetry 
                                SET `question`=%s,`answer`=%s,`remark`=%s,`update_time`=Now() 
                                WHERE `id`=%s"""
    IQ_VALIDATE_ALL_ID = """SELECT `id` FROM coco_home.todo_interesting_poetry"""
    IQ_VALIDATE_ANSWER = """SELECT `answer` FROM coco_home.todo_interesting_poetry WHERE id=%s AND answer=%s"""

    #驱动相关
    AGENT_SCRIPT_LIST = """SELECT `id`,`resource_id`,`name`,`py_version`,`is_alert_bind`,`is_target_bind`,`create_time`,
    `update_time`,`status`,`remark`,`update_by` FROM cocoa.drive_py_script WHERE `is_del`=0"""
    AGENT_SCRIPT_CODE = """SELECT path FROM cocoa.cc_resource 
                            WHERE `id` =(SELECT resource_id FROM cocoa.drive_py_script WHERE id=%s)"""
    AGENT_SCRIPT_CREATE = """INSERT INTO drive_py_script(`id`,`name`,`py_version`,
    `remark`,`resource_id`,`create_time`,`create_by`)VALUES (%s,%s,%s,%s,%s,NOW(),%s)"""
    



class CommonFunc:
    @staticmethod
    def kill_repeat(sql,*args):
        """文件类型校验去重"""
        result = db.fetch_one(sql,args)
        count = result.get("number")
        return True if count == 0 else False
