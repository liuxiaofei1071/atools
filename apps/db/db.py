# -*- coding: utf-8 -*-
# @Time : 2020/9/25 12:02
# @Author : Cassie Daddy
# @Email : liuxiaofeikeke@163.com
# @Site :
# @File : files_manager.py

import pymysql

from apps.conf import logger
from apps.conf.secure import (
    DB_USER,
    DB_HOST,
    DB_PORT,
    DB_PASSWORD,
    DATABASE
)

"""创建一个基于pymysql的操作类 主要用于对数据的增删改查"""


class DB:
    # 初始化/构造
    def __init__(self, host='127.0.0.1', port=3306, user='root', password='123', database='vod'):
        try:
            # 获取数据库连接/句柄
            self.coon = pymysql.connect(host=host, port=port, user=user, password=password, database=database)
            # 获取游标
            self.cursor = self.coon.cursor(cursor=pymysql.cursors.DictCursor)
        except Exception as e:
            logger.error(e)

    # 增
    def insert(self, sql):
        try:
            insert_id = self.cursor.execute(sql)
            self.coon.commit()
            return self.cursor.lastrowid
        except:
            self.coon.rollback()
            return 0

    # 删
    def delete(self, sql):
        try:
            del_id = self.cursor.execute(sql)
            self.coon.commit()
            return self.coon.affected_rows()
        except:
            self.coon.rollback()
            return 0

    # 改
    def update(self, sql):
        try:
            update_id = self.cursor.execute(sql)
            self.coon.commit()
            return self.coon.affected_rows()
        except:
            self.coon.rollback()
            return 0

    # 查
    def select(self, sql):
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            return data
        except:
            return []

    # 查一条记录
    def get_one(self, sql):
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchone()
        except:
            return {}

    # 析构函数
    def __del__(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.coon:
                self.coon.close()
        except:
            pass


db = DB(
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DATABASE
)
