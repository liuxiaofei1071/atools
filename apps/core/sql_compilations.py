# _*_ coding:utf-8 _*_
# @Time:2021/2/23 15:37
# @Author:Cassie·Lau
# @File sql_compilations.py

class SQLCompilations:
    """
    Distribution center
    """

    class User:
        CHECK = "SELECT COUNT(*) as number  FROM todo_user WHERE `nick_name`=%s OR `phone`=%s OR `email`=%s"

        GET_USER_ID = "SELECT `id` FROM todo_user WHERE `id`=%s"

        GET_USER = "SELECT `id`,`nick_name`,AES_DECRYPT(`password`,`salt`) AS `passwd` FROM todo_user WHERE `email`=%s OR `phone`=%s OR `nick_name`=%s "

        USER_STATUS = "SELECT status FROM todo_user  WHERE `id`=%s AND is_del=%s"

        CREATE_USER = """INSERT INTO todo_user(`id`,`nick_name`,`avatar`,`email`,`phone`,`password`,`salt`,`create_time`) 
                          VALUES (%s,%s,%s,%s,%s,aes_encrypt(%s,%s),%s,NOW())"""


    class ContentType:

        CREATE = """INSERT INTO cc_content_type(`id`,`filetype`,`name`,`suffix`,`create_time`,`create_by`,`update_time`,`update_by`)
          VALUES (%s,%s,%s,%s,NOW(),'admin',NOW(),'admin')"""

        GET_ONE = "SELECT `id`,`filetype`,`name`,`suffix` FROM cc_content_type WHERE `id`=%s"

        GET_LIST = "SELECT `id`,`filetype`,`name`,`suffix` FROM cc_content_type"

        CHECK = "SELECT COUNT(*) as number  FROM cc_content_type WHERE `filetype`=%s AND `suffix`=%s"

        GET_DIRECTION = "SELECT `name` FROM cc_content_type WHERE `filetype`=%s AND `suffix`=%s"

        DEL = "UPDATE cc_content_type SET `is_del`=1 WHERE id=%s"

    class Resource:
        CHECK = "SELECT COUNT(*) AS number FROM cc_resource WHERE `filename`=%s AND `is_del`=0"

        CREATE = """INSERT INTO cc_resource
                (`id`,`filename`,`size`,`suffix`,`path`,`create_by`,`create_time`)
            VALUES (%s,%s,%s,%s,%s,'admin',NOW())"""

        CODE_DEL = "UPDATE cc_resource SET `is_del`=1 WHERE id=(SELECT resource_id FROM drive_py_script WHERE id=%s)"

    class Agent:
        GET_LIST = """SELECT dps.*, tu.nick_name AS create_user FROM drive_py_script dps 
                               LEFT JOIN  todo_user tu ON dps.create_by = tu.id WHERE dps.`is_del`=0"""

        GET_CODE_PATH = """SELECT path FROM cc_resource 
                                WHERE `id` =(SELECT resource_id FROM drive_py_script WHERE id=%s AND `status`=1)"""

        CREATE = """INSERT INTO drive_py_script(`id`,`name`,`py_version`,`remark`,`resource_id`,
                                    `create_time`,`create_by`)
                    VALUES (%s,%s,%s,%s,%s,NOW(),%s)"""

        CHECK = "SELECT COUNT(*) as number  FROM drive_py_script WHERE `name`=%s"

        UPDATE = """UPDATE drive_py_script 
                    SET  `name`=%s,`py_version`=%s,`status`=%s,`remark`=%s,`update_by`=%s,`update_time`=Now() 
                    WHERE `id`=%s"""

        GET_ONE = "SELECT * FROM drive_py_script WHERE `id`=%s AND is_del=0"

        DEL_ONE = "UPDATE drive_py_script SET `is_del`=1 WHERE id=%s"