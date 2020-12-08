# -*- coding: utf-8 -*-
# @Time : 2020/9/25 12:02
# @Author : Cadman
# @Email : liuxiaofeikeke@163.com
# @Site :
# @File : files_manager.py

import pymysql

from apps.config.settings import logger
from apps.config.secure import (
    DB_USER,
    DB_HOST,
    DB_PORT,
    DB_PASSWORD,
    DATABASE
)


class MySQLDB:
    """创建一个基于pymysql的操作类 主要用于对数据的增删改查"""

    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        try:
            # 获取数据库连接/句柄
            self.coon = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            # 获取游标
            self.cursor = self.coon.cursor(cursor=pymysql.cursors.DictCursor)
        except Exception as e:
            logger.error(e)

    def insert_more(self, sql, args):
        try:
            self.cursor = self.coon.cursor()
            self.cursor.executemany(sql, args)
            self.coon.commit()
            return self.cursor.lastrowid
        except Exception as e:
            logger.error(e)
            self.coon.rollback()
            return 0

    def insert(self, sql, *args):
        """新增"""
        try:
            self.cursor = self.coon.cursor()
            self.cursor.execute(sql, args)
            self.coon.commit()
            return self.cursor.lastrowid
        except Exception as e:
            logger.error(e)
            self.coon.rollback()
            return 0

    def delete(self, sql, params):
        """删除"""
        try:
            self.cursor = self.coon.cursor()
            self.cursor.execute(sql, params)
            self.coon.commit()
            return self.coon.affected_rows()
        except Exception as e:
            logger.error(e)
            self.coon.rollback()
            return 0

    def update(self, sql, *args):
        """更新"""
        try:
            self.cursor = self.coon.cursor()
            self.cursor.execute(sql, args)
            self.coon.commit()
            return self.coon.affected_rows()
        except Exception as e:
            self.coon.rollback()
            logger.error(e)
            return 0

    def select_more(self, sql, *args):
        """查所有记录"""
        try:
            self.cursor = self.coon.cursor(cursor=pymysql.cursors.DictCursor)
            self.cursor.executemany(sql, args)
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            logger.error(e)
            return []

    def select(self, sql, params=None):
        """查所有记录"""
        try:
            self.cursor = self.coon.cursor(cursor=pymysql.cursors.DictCursor)
            if params:
                self.cursor.execute(sql, params)
            else:
                self.cursor.execute(sql)
            data = self.cursor.fetchall()

            return data
        except Exception as e:
            logger.error(e)
            return []

    def get_one(self, sql, *args):
        """查一条记录"""
        try:
            self.cursor = self.coon.cursor(cursor=pymysql.cursors.DictCursor)
            self.cursor.execute(sql, args)
            result = self.cursor.fetchone()
            return result if result else {}
        except Exception as e:
            logger.error(e)
            return {}

    # 析构函数
    def __del__(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.coon:
                self.coon.close()
        except Exception as e:
            logger.error(e)


db = MySQLDB(
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DATABASE
)
